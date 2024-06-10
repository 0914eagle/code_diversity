
def encrypt(s: str) -> str:
    def shift_letter(letter, shift):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        new_index = (alphabet.index(letter) + shift) % 26
        return alphabet[new_index]

    def encrypt_letter(letter):
        return shift_letter(letter, 2 * 2)

    encrypted_string = ''.join([encrypt_letter(char) for char in s])
    return encrypted_string

# Test cases
print(encrypt('hi'))
print(encrypt('asdfghjkl'))
print(encrypt('gf'))
print(encrypt('et'))
