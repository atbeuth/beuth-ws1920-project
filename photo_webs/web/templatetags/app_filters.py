from django import template

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
        if (term.upper() in image.title.upper()) or (term.upper() in image.description.upper()) or (term.upper() in image.long_description.upper()) or (term.upper() in image.category.upper()) or (term.upper() in image.user.username.upper()):
            return True
    return False