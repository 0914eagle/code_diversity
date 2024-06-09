
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
    plaintext = plaintext.replace(" ", "").replace("q", "")

    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext) - 1, 2):
        digraph = plaintext[i:i + 2]
        if digraph[0] == digraph[1]:
            digraph += "x"
        if digraph[0] in "abcdef":
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 1]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) + 1]
        elif digraph[0] in "ghijkl":
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 5]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 5]
        elif digraph[0] in "mnopqr":
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 10]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 10]
        elif digraph[0] in "stuvwx":
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 15]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 15]
        elif digraph[0] in "yz":
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 20]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 20]

    # If the plaintext has an odd number of characters, encrypt the last character
    if len(plaintext) % 2 == 1:
        encrypted_text += encryption_key[encryption_key.index(plaintext[-1]) + 1]

    return encrypted_text.upper()

