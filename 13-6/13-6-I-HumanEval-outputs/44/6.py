
def encode(message: str) -> str:
    
    encoded_message = ""
    for char in message:
        if char.isupper():
            encoded_message += chr(ord(char) + 32)
        else:
            encoded_message += chr(ord(char) - 32)
    
    vowels = ["a", "e", "i", "o", "u"]
    for i in range(len(encoded_message)):
        if encoded_message[i].lower() in vowels:
            index = vowels.index(encoded_message[i].lower())
            encoded_message = encoded_message[:i] + vowels[(index + 2) % 5] + encoded_message[i + 1:]
    
    return encoded_message

