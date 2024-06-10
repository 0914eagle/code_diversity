
def shift_left(char):
    if char in "qwertyuiop":
        return chr((ord(char) - 1) % 26 + ord('a'))
    elif char in "asdfghjkl;":
        return chr((ord(char) - 1) % 26 + ord('j'))
    elif char in "zxcvbnm,./":
        return chr((ord(char) - 1) % 26 + ord('m'))
    else:
        return char

def shift_right(char):
    if char in "qwertyuiop":
        return chr((ord(char) + 1) % 26 + ord('a'))
    elif char in "asdfghjkl;":
        return chr((ord(char) + 1) % 26 + ord('j'))
    elif char in "zxcvbnm,./":
        return chr((ord(char) + 1) % 26 + ord('m'))
    else:
        return char

def decode_message(direction, message):
    if direction == "L":
        return "".join([shift_left(char) for char in message])
    elif direction == "R":
        return "".join([shift_right(char) for char in message])
    else:
        return message

if __name__ == '__main__':
    direction = input()
    message = input()
    print(decode_message(direction, message))

