
def encode(message: str) -> str:
    
    # Create a dictionary to map vowels to their encoded values
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'm',
        'u': 's'
    }
    
    # Create a new string to store the encoded message
    encoded_message = ''
    
    # Iterate through each character in the message
    for char in message:
        # If the character is a vowel, use the encoded value from the dictionary
        if char.lower() in vowel_map:
            encoded_message += vowel_map[char.lower()]
        # If the character is not a vowel, swap its case
        else:
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
    
    return encoded_message

