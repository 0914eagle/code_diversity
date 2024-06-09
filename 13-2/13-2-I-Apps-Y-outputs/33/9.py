
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char != " " and char not in encryption_key:
            encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)

    # Remove spaces and duplicate letters from the plaintext
    plaintext = plaintext.replace(" ", "")
    plaintext = "".join(set(plaintext))

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext):
            digraph = plaintext[i:i+2]
        else:
            digraph = plaintext[i] + "X"
        row1 = encryption_key.index(digraph[0]) // 5
        col1 = encryption_key.index(digraph[0]) % 5
        row2 = encryption_key.index(digraph[1]) // 5
        col2 = encryption_key.index(digraph[1]) % 5
        if row1 == row2:
            encrypted_text += encryption_key[col1 + 1] + encryption_key[col2 + 1]
        elif col1 == col2:
            encrypted_text += encryption_key[row1 + 5] + encryption_key[row2 + 5]
        else:
            encrypted_text += encryption_key[row1 * 5 + col2] + encryption_key[row2 * 5 + col1]

    return encrypted_text.upper()

