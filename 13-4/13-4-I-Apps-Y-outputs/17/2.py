
def f1(encrypted_message, key):
    # Function to decrypt the message
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        # Get the position of the character in the key
        key_pos = key.index(encrypted_message[i])
        # If the index is even, shift the character forward by the key position
        if i % 2 == 0:
            decrypted_message += chr((ord(encrypted_message[i]) - key_pos) % 26 + ord('A'))
        # If the index is odd, shift the character backward by the key position
        else:
            decrypted_message += chr((ord(encrypted_message[i]) + key_pos) % 26 + ord('A'))
    return decrypted_message

def f2(encrypted_message, key):
    # Function to encrypt the message
    encrypted_message = ""
    for i in range(len(message)):
        # Get the position of the character in the key
        key_pos = key.index(message[i])
        # If the index is even, shift the character forward by the key position
        if i % 2 == 0:
            encrypted_message += chr((ord(message[i]) + key_pos) % 26 + ord('A'))
        # If the index is odd, shift the character backward by the key position
        else:
            encrypted_message += chr((ord(message[i]) - key_pos) % 26 + ord('A'))
    return encrypted_message

if __name__ == '__main__':
    message = input("Enter the message: ")
    key = input("Enter the key: ")
    encrypted_message = f2(message, key)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = f1(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

