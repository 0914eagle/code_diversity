
def encode(message: str) -> str:
    
    # Create a dictionary to map vowels to their encoded values
    vowels = {"a": "c", "e": "g", "i": "k", "o": "m", "u": "p"}
    
    # Create a new string to store the encoded message
    encoded_message = ""
    
    # Iterate through each character in the message
    for char in message:
        # If the character is a vowel, replace it with its encoded value
        if char.lower() in vowels:
            encoded_message += vowels[char.lower()]
        # If the character is a consonant, swap its case
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    
    return encoded_message

