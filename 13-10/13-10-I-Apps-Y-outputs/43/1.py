
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char.isalpha() and char.lower() not in encryption_key:
            encryption_key.append(char.lower())
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    encryption_key = "".join(encryption_key)

    # Encrypt the plaintext
    ciphertext = ""
    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            ciphertext += encryption_key[encryption_key.index(plaintext[i]) + 1]
            ciphertext += "x"
        elif encryption_key[encryption_key.index(plaintext[i]) + 1] == encryption_key[encryption_key.index(plaintext[i + 1])]:
            ciphertext += encryption_key[encryption_key.index(plaintext[i]) + 2]
        elif encryption_key[encryption_key.index(plaintext[i])] == encryption_key[encryption_key.index(plaintext[i + 1])]:
            ciphertext += encryption_key[encryption_key.index(plaintext[i + 1]) + 1]
        elif encryption_key[encryption_key.index(plaintext[i])] == encryption_key[encryption_key.index(plaintext[i + 1]) + 1]:
            ciphertext += encryption_key[encryption_key.index(plaintext[i]) + 1]
        else:
            ciphertext += encryption_key[encryption_key.index(plaintext[i + 1])]
    if len(plaintext) % 2 == 1:
        ciphertext += encryption_key[encryption_key.index(plaintext[-1]) + 1]
    return ciphertext.upper()

def main():
    key_phrase = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    print(playfair_cipher(key_phrase, plaintext))

if __name__ == '__main__':
    main()

