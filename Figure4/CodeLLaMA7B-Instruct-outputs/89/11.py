

def encrypt(s):
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # Calculate the encrypted character using the rotation formula
            encrypted_char = chr((ord(char) + 2 * 2 - ord('A')) % 26 + ord('A'))
        # Check if the character is lowercase
        elif char.islower():
            # Calculate the encrypted character using the rotation formula
            encrypted_char = chr((ord(char) + 2 * 2 - ord('a')) % 26 + ord('a'))
        # If the character is a space or a special character, add it to the encrypted message as is
        else:
            encrypted_char = char

        # Add the encrypted character to the end of the encrypted message
        encrypted_message += encrypted_char

    # Return the encrypted message
    return encrypted_message


