
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char != " " and char != "q":
            encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    encryption_key = "".join(encryption_key)

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i])]
        else:
            pair = plaintext[i:i+2]
            if pair[0] == pair[1]:
                pair += "x"
            row1 = encryption_key.index(pair[0]) // 5
            row2 = encryption_key.index(pair[1]) // 5
            col1 = encryption_key.index(pair[0]) % 5
            col2 = encryption_key.index(pair[1]) % 5
            if row1 == row2:
                encrypted_text += encryption_key[encryption_key.index(pair[0]) + 1]
                encrypted_text += encryption_key[encryption_key.index(pair[1]) + 1]
            elif col1 == col2:
                encrypted_text += encryption_key[encryption_key.index(pair[0]) + 5]
                encrypted_text += encryption_key[encryption_key.index(pair[1]) + 5]
            else:
                encrypted_text += encryption_key[encryption_key.index(pair[0]) + col2 - col1]
                encrypted_text += encryption_key[encryption_key.index(pair[1]) + col1 - col2]

    return encrypted_text.upper()

