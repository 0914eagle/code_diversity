
def solve(direction, message):
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
    
    if direction == 'L':
        return ''.join([keyboard[message[i-1]] for i in range(1, len(message))])
    else:
        return ''.join([keyboard[message[i+1]] for i in range(len(message)-1)])

