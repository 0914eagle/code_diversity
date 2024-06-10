
def get_neighbor(key, direction):
    if direction == 'L':
        return keyboard[keyboard.index(key) - 1]
    else:
        return keybaord[keyboard.index(key) + 1]

def decode_message(message, direction):
    decoded_message = ''
    for char in message:
        decoded_message += get_neighbor(char, direction)
    return decoded_message

def main():
    direction = input()
    message = input()
    print(decode_message(message, direction))

if __name__ == '__main__':
    main()

