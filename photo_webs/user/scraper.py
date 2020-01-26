import getopt
import ssl
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import json

class Profile:
    def __init__(self, instaUserData):
        self.id = instaUserData['id']
        self.fullname = instaUserData['full_name']
        self.username = instaUserData['username']
        self.profil_picture_path = instaUserData['profile_pic_url']

    def to_obj(self):
        return {
            'username': self.username,
            'fullname': self.fullname,
            'profilPicturePath': self.profil_picture_path
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_obj())

class Media:
    def __init__(self, media_node):
        self.pictureUrl = 'https://www.instagram.com/p/%s/'
        try:
            self.title = media_node['edge_media_to_caption']['edges'][0]['node']['text'].replace('"', '*/?"')
        except Exception as e:
            self.title = "<Could not parse title>"

        try:
            self.alt_text = media_node['accessibility_caption'].replace('"', '*/?"')
        except Exception as e:
            self.alt_text = "<Could not parse alternate text>"

        self.path = self.pictureUrl % (media_node['shortcode'])
        self.src = media_node['display_url']
        self.isVideo = media_node['is_video']

    def to_obj(self):
        return {
            "title": self.title,
            "altText": self.alt_text,
            "mediaPath": self.path,
            "mediaSrc": self.src,
            "isVideo": self.isVideo
        }

    def __repr__(self) -> str:
        return json.dumps(self.to_obj())

class InstagramImageScraper:

    def __init__(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.debug = False


        self.hashtagUrl = 'https://www.instagram.com/explore/tags/%s/'
        self.profilUrl = 'https://www.instagram.com/%s/'
        self.pictureUrl = 'https://www.instagram.com/p/%s/'
        self.graph_ql_url = 'https://www.instagram.com/graphql/query?query_hash=%s&variables=%s'
        self.media_query_hash = 'e769aa130647d2354c40ea6a439bfc08'

        self.media_variables = '{"id": "%s", "first": 12, "after": "%s"}'

    def get_shared_data(self, url):
        html = urllib.request.urlopen(url, context=self.ctx).read().decode("utf-8", "ignore")
        soup = BeautifulSoup(html, 'html.parser')
        script = soup.find('script', text=lambda t:
            t.startswith('window._sharedData'))

        return script

    def get_profile(self, instagramName):
        url = self.profilUrl % instagramName
        script = self.get_shared_data(url)
        if script:
            page_json = script.text.split(' = ', 1)[1].rstrip(';')
            data = json.loads(page_json)
            userData = data['entry_data']['ProfilePage'][0]['graphql']['user']
            return Profile(userData)
        else:
            print('No Data found')

    def get_dict(self, username):
        data = {
            'profile': {},
            'total': 0,
            'media': []
        }

        url = self.profilUrl % username
        script = self.get_shared_data(url)
        if script:
            page_json = script.text.split(' = ', 1)[1].rstrip(';')
            page_data = json.loads(page_json)
            userData = page_data['entry_data']['ProfilePage'][0]['graphql']['user']
            profile = Profile(userData)
            data['profile'] = profile.to_obj()

            timeline_media = userData['edge_owner_to_timeline_media']
            total_media = timeline_media['count']
            has_next_page = timeline_media['page_info']['has_next_page']
            end_cursor = timeline_media['page_info']['end_cursor']

            data['total'] = total_media

            for i, media_edge in enumerate(timeline_media['edges'], start=1):
                print('\rProcess: %d von %d' % (i, total_media), end='')
                try:
                    picture = Media(media_edge['node'])
                    data['media'].append(picture.to_obj())
                except Exception as e:
                    print(" --> Error occurred.")

            while has_next_page:

                try:

                    new_variables = urllib.parse.quote_plus(self.media_variables % (profile.id, end_cursor))
                    new_url = self.graph_ql_url % (self.media_query_hash, new_variables)
                    print('\nLoading next page ...')
                    media_response = urllib.request.urlopen(new_url, context=self.ctx).read().decode("utf-8")
                    media_json = json.loads(media_response)

                    has_next_page =  media_json['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
                    end_cursor =  media_json['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']

                    edges = media_json['data']['user']['edge_owner_to_timeline_media']['edges']
                    current_size = len(data['media'])
                    for i, media_edge in enumerate(edges, start=1):
                        print('\rProcess: %d von %d' % (current_size + i, total_media), end='')
                        try:
                            picture = Media(media_edge['node'])
                            data['media'].append(picture.to_obj())
                        except Exception as e:
                            print(" --> Error occurred.")
                except Exception as ee:

                    has_next_page = False
        else:
            print('No Data found')
        
        return data

