
def encode(message: str) -> str:
    
    # Create a dictionary to map vowels to their corresponding encoded values
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'm',
        'u': 'p'
    }
    
    # Create a new string to store the encoded message
    encoded_message = ''
    
    # Iterate through the message
    for char in message:
        # If the character is a vowel, use the encoded value from the dictionary
        if char.lower() in vowel_map:
            encoded_message += vowel_map[char.lower()]
        # If the character is a consonant, swap its case
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    
    return encoded_message

