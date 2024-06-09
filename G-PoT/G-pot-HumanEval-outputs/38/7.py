
def encrypt(s: str) -> str:
    encrypted_str = ""
    for char in s:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a') + 2) * 2) % 26 + ord('a'))
            encrypted_str += shifted_char
        else:
            encrypted_str += char
    return encrypted_str
