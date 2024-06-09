
def get_original_message(shift_direction, typed_message):
    keyboard = {
        "q": 0, "w": 1, "e": 2, "r": 3, "t": 4, "y": 5, "u": 6, "i": 7, "o": 8, "p": 9,
        "a": 10, "s": 11, "d": 12, "f": 13, "g": 14, "h": 15, "j": 16, "k": 17, "l": 18, ";": 19,
        "z": 20, "x": 21, "c": 22, "v": 23, "b": 24, "n": 25, "m": 26, ",": 27, ".": 28, "/": 29
    }
    original_message = ""
    for char in typed_message:
        x = keyboard[char]
        if shift_direction == "L":
            x = (x - 1) % 30
        else:
            x = (x + 1) % 30
        original_message += keyboard[list(keyboard)[x]]
    return original_message

