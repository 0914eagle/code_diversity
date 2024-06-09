
def get_smallest_unused_letter(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in letters:
        if letter not in s:
            return letter
    return 'None'

