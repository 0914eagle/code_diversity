
def get_original_message(direction, typed_message):
    keyboard = {
        'q': 'a', 'w': 's', 'e': 'd', 'r': 'f', 't': 'g', 'y': 'h', 'u': 'j', 'i': 'k', 'o': 'l', 'p': ';',
        'a': 'q', 's': 'w', 'd': 'e', 'f': 'r', 'g': 't', 'h': 'y', 'j': 'u', 'k': 'i', 'l': 'o', ';': 'p',
        'z': 'x', 'x': 'c', 'c': 'v', 'v': 'b', 'b': 'n', 'n': 'm', 'm': ',', ',': '.', '.': '/'
    }
    original_message = ""
    for char in typed_message:
        if direction == "L":
            original_message += keyboard[char]
        else:
            original_message += keyboard[char]
    return original_message

