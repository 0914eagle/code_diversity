
def vigenere_cipher(message, key, is_encrypt=True):
    
    # Convert the message and key to uppercase
    message = message.upper()
    key = key.upper()
    
    # Create a list to store the encrypted/decrypted message
    cipher_message = []
    
    # Loop through each character in the message
    for i, char in enumerate(message):
        # Find the index of the character in the alphabet
        char_index = ord(char) - ord('A')
        
        # Find the index of the key character
        key_index = ord(key[i % len(key)]) - ord('A')
        
        # Perform the encryption/decryption
        if is_encrypt:
            new_index = (char_index + key_index) % 26
        else:
            new_index = (char_index - key_index) % 26
        
        # Add the encrypted/decrypted character to the list
        cipher_message.append(chr(ord('A') + new_index))
    
    # Join the list of characters into a single string
    return ''.join(cipher_message)

def decrypt_message(encrypted_message, key):
    
    return vigenere_cipher(encrypted_message, key, is_encrypt=False)

if __name__ == '__main__':
    # Read the encrypted message and key from stdin
    encrypted_message = input()
    key = input()
    
    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, key)
    
    # Print the decrypted message
    print(decrypted_message)

