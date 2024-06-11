
def encrypt(s: str) -> str:
    def shift_letter(letter, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = (alphabet.index(letter) + shift) % 26
        return alphabet[index]

    encrypted = ''
    for char in s:
        encrypted += shift_letter(char, 2 * 2)
    
    return encrypted

# Test cases
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))