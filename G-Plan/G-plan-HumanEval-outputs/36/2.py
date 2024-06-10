
def encrypt(s: str) -> str:
    def shift_letter(letter, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_pos = (alphabet.index(letter) + shift) % 26
        return alphabet[new_pos]

    encrypted = ''
    for char in s:
        encrypted += shift_letter(char, 2 * 2)
    
    return encrypted

input_str = input()
print(encrypt(input_str))
