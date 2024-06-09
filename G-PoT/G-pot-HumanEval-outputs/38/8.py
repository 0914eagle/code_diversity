
def encrypt(s: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        if char.isalpha():
            idx = (alphabet.index(char) + 2) % 26
            encrypted += alphabet[idx]
        else:
            encrypted += char
    return encrypted
