
def encrypt(s: str) -> str:
    encrypted = ""
    for char in s:
        if char.isalpha():
            shifted = ord(char) + 2 * 2
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted
