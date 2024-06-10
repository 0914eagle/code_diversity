
def get_original_message(direction, typed_message):
    keyboard = {
        "q": "a",
        "w": "s",
        "e": "d",
        "r": "f",
        "t": "g",
        "y": "h",
        "u": "j",
        "i": "k",
        "o": "l",
        "p": ";",
        "a": "z",
        "s": "x",
        "d": "c",
        "f": "v",
        "g": "b",
        "h": "n",
        "j": "m",
        "k": ",",
        "l": ".",
        ";": "/"
    }
    original_message = ""
    for char in typed_message:
        if direction == "L":
            original_message += keyboard[char]
        elif direction == "R":
            original_message += keyboard[char]
    return original_message

def main():
    direction = input("Enter the direction of shifting (L or R): ")
    typed_message = input("Enter the typed message: ")
    original_message = get_original_message(direction, typed_message)
    print(original_message)

if __name__ == '__main__':
    main()

