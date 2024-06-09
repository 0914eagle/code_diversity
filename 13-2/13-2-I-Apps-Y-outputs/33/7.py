
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
    for i in range(0, len(plaintext) - 1, 2):
        digraph = plaintext[i:i + 2]
        if digraph[0] == digraph[1]:
            digraph += "x"
        if digraph[0] == "x":
            encrypted_text += digraph[1]
        elif digraph[1] == "x":
            encrypted_text += digraph[0]
        else:
            row1 = encryption_key.index(digraph[0]) // 5
            row2 = encryption_key.index(digraph[1]) // 5
            col1 = encryption_key.index(digraph[0]) % 5
            col2 = encryption_key.index(digraph[1]) % 5
            if row1 == row2:
                encrypted_text += encryption_key[col1 + 1]
                encrypted_text += encryption_key[col2 + 1]
            elif col1 == col2:
                encrypted_text += encryption_key[row1 * 5 + (col1 + 1) % 5]
                encrypted_text += encryption_key[row2 * 5 + (col2 + 1) % 5]
            else:
                encrypted_text += encryption_key[row1 * 5 + col2]
                encrypted_text += encryption_key[row2 * 5 + col1]

    return encrypted_text.upper()

