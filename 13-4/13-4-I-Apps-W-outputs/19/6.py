
def get_original_message(shift_direction, typed_message):
    keyboard = {
        'q': 'q',
        'w': 'w',
        'e': 'e',
        'r': 'r',
        't': 't',
        'y': 'y',
        'u': 'u',
        'i': 'i',
        'o': 'o',
        'p': 'p',
        'a': 'a',
        's': 's',
        'd': 'd',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'z': 'z',
        'x': 'x',
        'c': 'c',
        'v': 'v',
        'b': 'b',
        'n': 'n',
        'm': 'm',
        ',': ',',
        '.': '.',
        '/': '/'
    }

    if shift_direction == 'L':
        shifted_keyboard = {
            'q': 'p',
            'w': 'o',
            'e': 'i',
            'r': 'u',
            't': 'y',
            'y': 't',
            'u': 'r',
            'i': 'e',
            'o': 'w',
            'p': 'q',
            'a': 'm',
            's': 'l',
            'd': 'k',
            'f': 'j',
            'g': 'h',
            'h': 'g',
            'j': 'f',
            'k': 'd',
            'l': 's',
            'z': 'x',
            'x': 'z',
            'c': 'v',
            'v': 'b',
            'b': 'n',
            'n': 'm',
            'm': 'b',
            ',': ';',
            ';': ',',
            '.': '/',
            '/': '.'
        }
    else:
        shifted_keyboard = {
            'q': 'a',
            'w': 's',
            'e': 'd',
            'r': 'f',
            't': 'g',
            'y': 'h',
            'u': 'j',
            'i': 'k',
            'o': 'l',
            'p': ';',
            'a': 'q',
            's': 'w',
            'd': 'e',
            'f': 'r',
            'g': 't',
            'h': 'y',
            'j': 'u',
            'k': 'i',
            'l': 'o',
            'z': 'p',
            'x': 'a',
            'c': 'z',
            'v': 'x',
            'b': 'c',
            'n': 'v',
            'm': 'b',
            ',': 'n',
            ';': 'm',
            '.': ',',
            '/': '.'
        }

    original_message = ''
    for char in typed_message:
        original_message += shifted_keyboard[char]

    return original_message

