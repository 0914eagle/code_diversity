
def shift_char(char, direction, shift):
    if direction == 'L':
        return chr(ord(char) - shift)
    else:
        return chr(ord(char) + shift)

def decode_message(message, direction, shift):
    decoded_message = ''
    for char in message:
        decoded_message += shift_char(char, direction, shift)
    return decoded_message

def main():
    direction = input()
    message = input()
    shift = 1
    decoded_message = decode_message(message, direction, shift)
    print(decoded_message)

if __name__ == '__main__':
    main()

