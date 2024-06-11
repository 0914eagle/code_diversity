

def encode(message):
    
    # Initialize an empty string to store the encoded message
    encoded_message = ""

    # Iterate through each character in the message
    for char in message:
        # Check if the character is a letter
        if char.isalpha():
            # If the character is a letter, swap case
            if char.islower():
                encoded_message += char.upper()
            else:
                encoded_message += char.lower()
        # Check if the character is a vowel
        elif char.isalpha() and char.islower():
            # If the character is a vowel, replace it with the letter 2 places ahead
            vowel_index = "aeiou".index(char)
            encoded_message += "abcdefghijklmnopqrstuvwxyz"[vowel_index + 2]
        else:
            # If the character is not a letter or vowel, add it to the encoded message as is
            encoded_message += char

    return encoded_message


