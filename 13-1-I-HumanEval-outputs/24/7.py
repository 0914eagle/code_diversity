
def encrypt(s: str) -> str:
    
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            encrypted_string += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            encrypted_string += char
    return encrypted_string

