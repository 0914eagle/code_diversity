
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
            elif encryption_key.index(digraph[0]) == encryption_key.index(digraph[1]):
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 1] + encryption_key[encryption_key.index(digraph[1]) + 1]
            elif encryption_key.index(digraph[0]) + 5 == encryption_key.index(digraph[1]):
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 1] + encryption_key[encryption_key.index(digraph[1]) - 4]
            else:
                encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 5] + encryption_key[encryption_key.index(digraph[1]) + 5]

    return encrypted_text

