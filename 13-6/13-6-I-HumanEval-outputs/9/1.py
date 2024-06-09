
def encrypt(s: str) -> str:
    
    encrypted_str = ""
    for char in s:
        if char.isalpha():
            encrypted_str += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            encrypted_str += char
    return encrypted_str

