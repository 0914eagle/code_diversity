
def encrypt(s: str) -> str:
    encrypted = ""
    for char in s:
        if char.isalpha():
            shift = 2 * ord(char) - 2
            if char.islower():
                encrypted += chr((shift - ord('a')) % 26 + ord('a'))
            else:
                encrypted += chr((shift - ord('A')) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted
