
def encrypt_message(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i]
        if i % 2 == 0:
            encrypted_message += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
        else:
            encrypted_message += chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i]
        if i % 2 == 0:
            decrypted_message += chr((ord(char) + ord(key_char) - 2 * ord('A')) % 26 + ord('A'))
        else:
            decrypted_message += chr((ord(char) - ord(key_char) + 26) % 26 + ord('A'))
    return decrypted_message

if __name__ == '__main__':
    message = input("Enter message: ")
    key = input("Enter key: ")
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

