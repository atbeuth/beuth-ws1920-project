from django import template

register = template.Library()

@register.filter(name='get_search_description')
def get_search_description(key):
    search_dict = {
        "Wallpaper": {
            "text": "Awesome wallpapers for your desktop",
            "suggestions": ["Nature", "Human", "Animals", "Portrait", "Photography", "World"]
        },
        "Free To Use": {
            "text": "This pictures are using the PhotoHub license",
            "suggestions": ["Humans", "Wallpaper", "Buildings", "Animals", "Portrait", "Photography", "World"]
        },
        "Nature": {
            "text": "Wonderful pictures from our blue planet",
            "suggestions": ["Space", "Trees", "Food", "Wallpaper", "Buildings", "Animals", "Photography", "World"]
        }
    }
    return search_dict.get(key)

@register.filter(name='dict_key')
def dict_key(d, k):
    '''Returns the given key from a dictionary.'''
    return d[k]