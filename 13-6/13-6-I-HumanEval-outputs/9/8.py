
def encrypt(s: str) -> str:
    
    encrypted_str = ""
    for char in s:
        if char.isalpha():
            encrypted_str += chr((ord(char) + 2*2 - 97) % 26 + 97)
        else:
            encrypted_str += char
    return encrypted_str

