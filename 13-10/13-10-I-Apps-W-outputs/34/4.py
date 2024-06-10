
def get_shifted_char(char, direction):
    if direction == "L":
        return chr(ord(char) - 1)
    else:
        return chr(ord(char) + 1)

def decode_message(message, direction):
    decoded_message = ""
    for char in message:
        decoded_message += get_shifted_char(char, direction)
    return decoded_message

def main():
    direction = input()
    message = input()
    print(decode_message(message, direction))

if __name__ == '__main__':
    main()

