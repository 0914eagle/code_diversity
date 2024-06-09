
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
        if plaintext[i] == plaintext[i + 1]:
            encrypted_text += plaintext[i] + "x"
        elif plaintext[i] in "abcdef":
            encrypted_text += encryption_key[encryption_key.index(plaintext[i + 1]) + 1]
        elif plaintext[i + 1] in "abcdef":
            encrypted_text += encryption_key[encryption_key.index(plaintext[i]) + 1]
        else:
            encrypted_text += encryption_key[encryption_key.index(plaintext[i]) // 5 * 5 + (encryption_key.index(plaintext[i + 1]) % 5) + 1]

    return encrypted_text.upper()

