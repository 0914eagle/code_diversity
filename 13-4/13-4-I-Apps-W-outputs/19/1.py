
def solve(direction, typed_sequence):
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
        ';': ';',
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
    
    if direction == 'L':
        return ''.join([keyboard.get(typed_sequence[i-1], '') for i in range(1, len(typed_sequence)+1)])
    else:
        return ''.join([keyboard.get(typed_sequence[i+1], '') for i in range(len(typed_sequence))])

