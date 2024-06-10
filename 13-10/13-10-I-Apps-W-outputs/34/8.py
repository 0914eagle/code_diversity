
def get_original_message(direction, shifted_message):
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
        original_message = ''
        for char in shifted_message:
            original_message += keyboard[char]
        return original_message
    elif direction == 'R':
        original_message = ''
        for char in shifted_message:
            original_message += keyboard[char]
        return original_message
    else:
        return 'Invalid input'

def main():
    direction = input()
    shifted_message = input()
    print(get_original_message(direction, shifted_message))

if __name__ == '__main__':
    main()

