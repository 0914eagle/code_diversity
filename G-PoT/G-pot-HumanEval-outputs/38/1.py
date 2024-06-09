
def encrypt(s: str) -> str:
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * ord(char) - 2
            if char.islower():
                encrypted += chr((ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted
