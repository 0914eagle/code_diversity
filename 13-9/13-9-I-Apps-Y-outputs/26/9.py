
def encrypt(message, key):
    # Encrypt the message using the Vigenère cipher
    encrypted_message = ""
    for i in range(len(message)):
        if i % 2 == 0:
            # Encrypt the character using the key
            encrypted_message += chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            # Decrypt the character using the key
            encrypted_message += chr((ord(message[i]) - ord(key[i]) + 26) % 26 + ord('A'))
    return encrypted_message

def decrypt(encrypted_message, key):
    # Decrypt the encrypted message using the Vigenère cipher
    message = ""
    for i in range(len(encrypted_message)):
        if i % 2 == 0:
            # Decrypt the character using the key
            message += chr((ord(encrypted_message[i]) - ord(key[i]) + 26) % 26 + ord('A'))
        else:
            # Encrypt the character using the key
            message += chr((ord(encrypted_message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return message

if __name__ == '__main__':
    message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    print(f"Decrypted message: {decrypt(message, key)}")

