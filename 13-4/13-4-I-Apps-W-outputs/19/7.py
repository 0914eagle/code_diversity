
def get_original_message(direction, shifted_message):
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    original_message = ""
    for char in shifted_message:
        index = keyboard.index(char)
        if direction == "L":
            new_index = index - 1
        else:
            new_index = index + 1
        original_message += keyboard[new_index]
    return original_message

