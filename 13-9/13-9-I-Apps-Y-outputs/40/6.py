
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = []
    for char in key_phrase:
        if char.isalpha() and char.lower() not in encryption_key:
            encryption_key.append(char.lower())
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key.append(char)
    
    # Split the plaintext into digraphs
    digraphs = []
    for i in range(0, len(plaintext) - 1, 2):
        digraphs.append(plaintext[i:i+2])
    if len(plaintext) % 2 == 1:
        digraphs.append(plaintext[-1])
    
    # Encrypt the digraphs
    encrypted_text = ""
    for digraph in digraphs:
        if len(digraph) == 1:
            encrypted_text += "X" + digraph
        elif len(digraph) == 2:
            i = encryption_key.index(digraph[0])
            j = encryption_key.index(digraph[1])
            if i == j:
                encrypted_text += "X" + digraph[0]
            elif i < j:
                encrypted_text += encryption_key[i+1] + encryption_key[j+1]
            else:
                encrypted_text += encryption_key[i-1] + encryption_key[j-1]
    
    return encrypted_text.upper()

