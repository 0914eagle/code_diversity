

def encrypt(s):
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Rotate the character by 2 places in the alphabet
            encrypted_char = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
        # Check if the character is lowercase
        elif char.islower():
            # Rotate the character by 2 places in the alphabet
            encrypted_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        # If the character is a space or a special character, leave it unchanged
        else:
            encrypted_char = char

        # Add the encrypted character to the end of the encrypted message
        encrypted_message += encrypted_char

    # Return the encrypted message
    return encrypted_message


