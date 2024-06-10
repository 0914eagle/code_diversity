
def encrypt(message, key):
    enc_message = ""
    for i in range(len(message)):
        if i % 2 == 0:
            enc_message += chr((ord(message[i]) + ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
        else:
            enc_message += chr((ord(message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return enc_message

def decrypt(enc_message, key):
    message = ""
    for i in range(len(enc_message)):
        if i % 2 == 0:
            message += chr((ord(enc_message[i]) - ord(key[i]) + 2 * ord('A')) % 26 + ord('A'))
        else:
            message += chr((ord(enc_message[i]) - ord(key[i]) - 2 * ord('A')) % 26 + ord('A'))
    return message

if __name__ == '__main__':
    message = input("Enter message: ")
    key = input("Enter key: ")
    enc_message = encrypt(message, key)
    print(f"Encrypted message: {enc_message}")
    dec_message = decrypt(enc_message, key)
    print(f"Decrypted message: {dec_message}")

