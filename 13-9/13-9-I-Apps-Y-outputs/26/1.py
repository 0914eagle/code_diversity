
def decrypt(encrypted_message, key):
    # Initialize variables
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_message = ""
    
    # Iterate through the encrypted message
    for i in range(len(encrypted_message)):
        # Get the current character in the encrypted message
        current_char = encrypted_message[i]
        
        # If the current character is an uppercase letter, decrypt it
        if current_char in alphabet:
            # Get the position of the current character in the alphabet
            current_pos = alphabet.index(current_char)
            
            # Get the key character at the current position
            key_char = key[i]
            
            # Get the position of the key character in the alphabet
            key_pos = alphabet.index(key_char)
            
            # If the current position is even, decrypt the character using the key
            if i % 2 == 0:
                # Decrypt the character by shifting it forwards by the key position
                decrypted_char = alphabet[(current_pos + key_pos) % len(alphabet)]
            
            # If the current position is odd, decrypt the character using the key
            else:
                # Decrypt the character by shifting it backwards by the key position
                decrypted_char = alphabet[(current_pos - key_pos) % len(alphabet)]
            
            # Add the decrypted character to the decrypted message
            decrypted_message += decrypted_char
        
        # If the current character is not an uppercase letter, add it to the decrypted message as is
        else:
            decrypted_message += current_char
    
    # Return the decrypted message
    return decrypted_message

def main():
    # Get the encrypted message and key from the user
    encrypted_message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    
    # Decrypt the message
    decrypted_message = decrypt(encrypted_message, key)
    
    # Print the decrypted message
    print(f"The decrypted message is: {decrypted_message}")

if __name__ == '__main__':
    main()

