
def encrypt(s: str) -> str:
    
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            encrypted_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_string += encrypted_char
    return encrypted_string

