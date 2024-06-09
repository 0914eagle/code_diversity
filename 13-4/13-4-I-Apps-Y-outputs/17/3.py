
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted_message += chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            encrypted_message += chr((ord(message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return encrypted_message

def decrypt(encrypted_message, key):
    message = ""
    for i in range(len(encrypted_message)):
        if i % 2 == 0:
            message += chr((ord(encrypted_message[i]) - ord(key[i]) + 2 * ord('A')) % 26 + ord('A'))
        else:
            message += chr((ord(encrypted_message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return message

if __name__ == '__main__':
    message = input("Enter message: ")
    key = input("Enter key: ")
    encrypted_message = encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

