
def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i]
        if i % 2 == 0:
            shift = ord(key_char) - ord('A')
        else:
            shift = 26 - (ord(key_char) - ord('A'))
        encrypted_message += chr((ord(char) + shift) % 26 + ord('A'))
    return encrypted_message

def decrypt(encrypted_message, key):
    message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i]
        if i % 2 == 0:
            shift = 26 - (ord(key_char) - ord('A'))
        else:
            shift = ord(key_char) - ord('A')
        message += chr((ord(char) - shift) % 26 + ord('A'))
    return message

if __name__ == '__main__':
    encrypted_message = input("Enter the encrypted message: ")
    key = input("Enter the key: ")
    print(decrypt(encrypted_message, key))

