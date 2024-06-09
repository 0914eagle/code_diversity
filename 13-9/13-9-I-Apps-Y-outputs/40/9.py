
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char != " " and char not in encryption_key:
            encryption_key.append(char)
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    
    # Remove spaces and convert to upper case
    plaintext = plaintext.upper().replace(" ", "")
    
    # Encrypt the message
    encrypted_text = ""
    for i in range(0, len(plaintext) - 1, 2):
        digraph = plaintext[i:i+2]
        if digraph[0] == digraph[1]:
            encrypted_text += "X"
        elif digraph[0] in encryption_key[0:5] and digraph[1] in encryption_key[0:5]:
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) + 1]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) + 1]
        elif digraph[0] in encryption_key[5:10] and digraph[1] in encryption_key[5:10]:
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 5]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 5]
        elif digraph[0] in encryption_key[10:15] and digraph[1] in encryption_key[10:15]:
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 10]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 10]
        elif digraph[0] in encryption_key[15:20] and digraph[1] in encryption_key[15:20]:
            encrypted_text += encryption_key[encryption_key.index(digraph[0]) - 15]
            encrypted_text += encryption_key[encryption_key.index(digraph[1]) - 15]
    
    return encrypted_text

