

def encrypt(s):
    
    # Initialize an empty string to store the encrypted message
    encrypted_message = ""

    # Loop through each character in the input string
    for char in s:
        # Check if the character is uppercase
        if char.isupper():
            # If it is uppercase, shift it down by two multiplied to two places in the alphabet
            encrypted_message += chr((ord(char) - ord('A') + 2 * 2) % 26 + ord('A'))
        # Otherwise, the character is lowercase
        else:
            # Shift it down by two multiplied to two places in the alphabet
            encrypted_message += chr((ord(char) - ord('a') + 2 * 2) % 26 + ord('a'))

    # Return the encrypted message
    return encrypted_message


