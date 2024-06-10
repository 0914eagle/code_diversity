
def encrypt_message(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted_message += chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            encrypted_message += chr((ord(message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return encrypted_message

def decrypt_message(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        if i % 2 == 0:
            decrypted_message += chr((ord(encrypted_message[i]) - ord(key[i]) + 2 * ord('A')) % 26 + ord('A'))
        else:
            decrypted_message += chr((ord(encrypted_message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return decrypted_message

if __name__ == '__main__':
    message = input("Enter message: ")
    key = input("Enter key: ")
    encrypted_message = encrypt_message(message, key)
    print("Encrypted message:", encrypted_message)
    decrypted_message = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

