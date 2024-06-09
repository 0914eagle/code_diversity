
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char not in encryption_key and char != " ":
            encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    encryption_key = "".join(encryption_key)

    # Remove spaces and duplicate letters from the plaintext
    plaintext = plaintext.replace(" ", "")
    plaintext = "".join(set(plaintext))

    # Encrypt the message
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext):
            digraph = plaintext[i:i+2]
        else:
            digraph = plaintext[i] + "X"
        if digraph[0] == digraph[1]:
            encrypted_text += "X"
        elif encryption_key.find(digraph[0]) > encryption_key.find(digraph[1]):
            encrypted_text += encryption_key[encryption_key.find(digraph[1]) + 1]
            encrypted_text += encryption_key[encryption_key.find(digraph[0]) + 1]
        elif encryption_key.find(digraph[0]) == encryption_key.find(digraph[1]):
            encrypted_text += encryption_key[encryption_key.find(digraph[0]) + 1]
            encrypted_text += encryption_key[encryption_key.find(digraph[1]) + 1]
        else:
            encrypted_text += encryption_key[encryption_key.find(digraph[0]) + 1]
            encrypted_text += encryption_key[encryption_key.find(digraph[1]) - 1]

    return encrypted_text.upper()

