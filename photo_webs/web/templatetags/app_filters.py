from django import template
import json

from random import sample

register = template.Library()


@register.filter(name='get_search_description')
def get_search_description(key):
    search_dict = {
        "ALPHABET": {
            "text": "",
            "suggestions": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        },
        "WALLPAPER": {
            "text": "Awesome wallpapers for your desktop",
            "suggestions": ["Nature", "Human", "Animals", "Portrait", "Photography", "World"]
        },
        "FREE TO USE": {
            "text": "This pictures are using the PhotoHub license",
            "suggestions": ["Humans", "Wallpaper", "Buildings", "Animals", "Portrait", "Photography", "World"]
        },
        "NATURE": {
            "text": "Wonderful pictures from our blue planet",
            "suggestions": ["Space", "Trees", "Food", "Wallpaper", "Buildings", "Animals", "Photography", "World"]
        },
        "SPORTS": {
            "text": "Wonderful sport pictures",
            "suggestions": ["Football", "Basketball", "Tennis", "Race", "Match", "Champion", "League"]
        },
        "BUILDING": {
            "text": "Nice pictures of buildings",
            "suggestions": ["city", "skyline", "house", "mosque", "church", "bridge"]
        },

        "ANIMALS": {
            "text": "Beautiful animals of our planet",
            "suggestions": ["monkey", "lion", "elefant", "bird", "fish"]
        },

        "TRAVEL": {
            "text": "Ideas for your next trip? ",
            "suggestions": ["trip", "travel", "hotel", "sea", "mountain", "relax"]
        },
        "PORTRAITS": {
            "text": "Beautiful faces and portrait pictures",
            "suggestions": ["face", "eyes", "mouth", "nose", "ears", "hair"]
        },

        "INTEREST": {
            "text": "Interest from a Person",
            "suggestions": ["Anime", "Gaming", "Manga", "Animations"]
        }
    }
    return search_dict.get(key.upper())


@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]


@register.filter(name='is_image_in_search')
def is_image_in_search(search, image):
    '''Returns true if the images is a result of the seacrh'''
    for term in search.split(" "):
        if (term.upper() in image.tags.upper()) or (term.upper() in image.title.upper()) or (term.upper() in image.description.upper()) or (term.upper() in image.long_description.upper()) or (term.upper() in image.category.upper()) or (term.upper() in image.user.username.upper()):
            return True
    return False


@register.filter(name='is_user_in_search')
def is_user_in_search(search, user):
    for term in search.split(" "):
        if (term.upper() in user.username.upper()) or (term.upper() in user.profile.bio.upper()) or (term.upper() in user.profile.bio_short.upper()):
            return True
    return False


@register.filter(name='split_text')
def split_text(text, split_on="\n"):
    return text.split(split_on)


@register.filter(name='int_to_list_string')
def int_to_list_string(num):
    int_string = ''
    for count in range(1, num + 1):
        int_string += str(count)
    return int_string


@register.filter(name='to_string')
def to_string(num):
    return str(num)


@register.filter(name='to_insta_post')
def to_insta_post(poststring):
    post_list = []

    post_list_temp = poststring.split("},")

    list_size = len(post_list_temp)

    max_imgs = 12

    if list_size <= max_imgs:
        post_list_choices = post_list_temp
    else:
        post_list_choices = sample(post_list_temp, max_imgs)

    for current_post_string in post_list_choices:
        try:
            current_post_json = json.loads(current_post_string.replace("[", "").replace(
                "'", '"').replace('*/?"', "'").replace("True", "true").replace("False", "false") + "}")
            post_list.append(current_post_json)
        except Exception as e:
            print(e)

    return post_list
