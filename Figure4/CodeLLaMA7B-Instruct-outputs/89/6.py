

def encrypt(s):
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # If it is uppercase, rotate it by 2 * 2 = 4 positions in the alphabet
            encrypted_char = chr((ord(char) - ord('A') + 4) % 26 + ord('A'))
        # Check if the character is lowercase
        elif char.islower():
            # If it is lowercase, rotate it by 2 * 2 = 4 positions in the alphabet
            encrypted_char = chr((ord(char) - ord('a') + 4) % 26 + ord('a'))
        # If the character is a space or a special character, leave it unchanged
        else:
            encrypted_char = char

        # Append the encrypted character to the encrypted message
        encrypted_message += encrypted_char

    # Return the encrypted message
    return encrypted_message


