
def solve(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter not in s:
            return letter
    return 'None'

