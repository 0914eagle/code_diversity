
def encrypt(s: str) -> str:
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * ord(char) - 2
            if char.islower():
                encrypted += chr((ord('a') + (ord(char) - ord('a') + shift) % 26))
            else:
                encrypted += chr((ord('A') + (ord(char) - ord('A') + shift) % 26))
        else:
            encrypted += char
    return encrypted
