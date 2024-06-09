
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char != " " and char not in encryption_key:
            encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    encryption_key = "".join(encryption_key)

    # Remove spaces and duplicate letters from the plaintext
    plaintext = plaintext.replace(" ", "")
    plaintext = "".join(set(plaintext))

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i])]
        elif plaintext[i] == plaintext[i + 1]:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i])] + "X"
        elif encryption_key.index(plaintext[i]) == encryption_key.index(plaintext[i + 1]):
            encrypted_text += encryption_key[encryption_key.index(plaintext[i]) + 1]
        elif encryption_key.index(plaintext[i]) // 5 == encryption_key.index(plaintext[i + 1]) // 5:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i + 1]) + 5 - encryption_key.index(plaintext[i]) % 5]
        else:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i]) // 5 * 5 + encryption_key.index(plaintext[i + 1]) % 5]

    return encrypted_text.upper()

