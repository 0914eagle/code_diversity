

def encode(message):
    
    # Initialize an empty string to store the encoded message
    encoded_message = ""

    # Iterate through each character in the message
    for char in message:
        # Check if the character is a vowel
        if char in "aeiou":
            # If it is a vowel, get the letter that appears 2 places ahead of it in the alphabet
            encoded_char = chr((ord(char) + 2) % 26 + ord('a'))
        else:
            # If it is not a vowel, simply swap the case
            if char.islower():
                encoded_char = char.upper()
            else:
                encoded_char = char.lower()

        # Add the encoded character to the encoded message
        encoded_message += encoded_char

    # Return the encoded message
    return encoded_message


