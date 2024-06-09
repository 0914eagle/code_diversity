
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
        if i == len(plaintext) - 1:
            encrypted_text += plaintext[i].upper()
        else:
            digraph = plaintext[i:i+2]
            if digraph[0] == digraph[1]:
                encrypted_text += digraph[0] + "X"
            elif digraph[0] in "abcdef" and digraph[1] in "abcdef":
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 1] + encryption_key[encryption_key.index(digraph[1]) + 1]
            elif digraph[0] in "ghijkl" and digraph[1] in "ghijkl":
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 5] + encryption_key[encryption_key.index(digraph[1]) - 5]
            elif digraph[0] in "mnopqr" and digraph[1] in "mnopqr":
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 10] + encryption_key[encryption_key.index(digraph[1]) - 10]
            elif digraph[0] in "stuvwx" and digraph[1] in "stuvwx":
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 15] + encryption_key[encryption_key.index(digraph[1]) - 15]
            elif digraph[0] in "yz" and digraph[1] in "yz":
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 20] + encryption_key[encryption_key.index(digraph[1]) - 20]
            else:
                encrypted_text += "X" + encryption_key[encryption_key.index(digraph[0])] + encryption_key[encryption_key.index(digraph[1])]

    return encrypted_text.upper()

