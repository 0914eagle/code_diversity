
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char != " ":
            if char not in encryption_key:
                encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    encryption_key = "".join(encryption_key)

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            encrypted_text += plaintext[i] + "x"
        elif plaintext[i] in encryption_key[5:]:
            row = encryption_key.index(plaintext[i]) // 5
            col = encryption_key.index(plaintext[i + 1]) // 5
            if row == col:
                encrypted_text += encryption_key[row * 5 + (col + 1) % 5]
            else:
                encrypted_text += encryption_key[row * 5 + col]
        else:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i]) + 5]
    if len(plaintext) % 2 == 1:
        encrypted_text += encryption_key[encryption_key.index(plaintext[-1]) + 5]

    return encrypted_text.upper()

