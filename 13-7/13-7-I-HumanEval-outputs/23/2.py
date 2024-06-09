
def encode(message: str) -> str:
    
    # Create a dictionary to map vowels to their encoded values
    vowel_map = {
        'a': 'c',
        'e': 'g',
        'i': 'k',
        'o': 'm',
        'u': 'p'
    }
    
    # Create a list to hold the encoded message
    encoded_message = []
    
    # Iterate through each character in the message
    for char in message:
        # If the character is a vowel, use the encoded value from the dictionary
        if char.lower() in vowel_map:
            encoded_message.append(vowel_map[char.lower()])
        # If the character is a consonant, swap its case
        else:
            encoded_message.append(char.swapcase())
    
    # Join the encoded message into a string and return it
    return ''.join(encoded_message)

