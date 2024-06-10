
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        if i % 2 == 0:
            encrypted_message += chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            encrypted_message += chr((ord(message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        if i % 2 == 0:
            decrypted_message += chr((ord(encrypted_message[i]) - ord(key[i]) + 2 * ord('A')) % 26 + ord('A'))
        else:
            decrypted_message += chr((ord(encrypted_message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return decrypted_message

if __name__ == '__main__':
    message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    print(f"Decrypted message: {decrypt(message, key)}")

