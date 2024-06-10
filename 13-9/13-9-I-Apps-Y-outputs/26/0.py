
def decrypt_message(encrypted_message, key):
    # Initialize variables
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ""
    
    # Iterate through the encrypted message
    for i, char in enumerate(encrypted_message):
        # Get the index of the character in the key
        key_index = alphabet.index(key[i])
        
        # If the index is even, shift the character forward by the key index
        if i % 2 == 0:
            decrypted_message += alphabet[(alphabet.index(char) + key_index) % len(alphabet)]
        # If the index is odd, shift the character backward by the key index
        else:
            decrypted_message += alphabet[(alphabet.index(char) - key_index) % len(alphabet)]
    
    return decrypted_message

