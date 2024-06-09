
def playfair_cipher(key_phrase, plaintext):
    # Create a 5x5 matrix with the key phrase
    key_matrix = []
    for i in range(5):
        key_matrix.append([])
        for j in range(5):
            if i * 5 + j < len(key_phrase):
                key_matrix[i].append(key_phrase[i * 5 + j])
            else:
                key_matrix[i].append(' ')
    
    # Remove spaces and duplicate letters from the key phrase
    key_phrase = ''.join([c for c in key_phrase if c not in ' '])
    key_phrase = ''.join(dict.fromkeys(key_phrase))
    
    # Fill the remaining spaces with the rest of the letters of the alphabet
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == ' ':
                key_matrix[i][j] = key_phrase[5 * i + j]
    
    # Encrypt the plaintext
    encrypted_text = ''
    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            encrypted_text += plaintext[i] + 'X'
        elif plaintext[i] in key_matrix[0]:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[i]) + 1) % 5] + key_matrix[1][(key_matrix[1].index(plaintext[i + 1]) + 1) % 5]
        elif plaintext[i + 1] in key_matrix[0]:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[i + 1]) + 1) % 5] + key_matrix[1][(key_matrix[1].index(plaintext[i]) + 1) % 5]
        elif plaintext[i] in key_matrix[1]:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[i + 1]) + 1) % 5] + key_matrix[1][(key_matrix[1].index(plaintext[i]) + 1) % 5]
        elif plaintext[i + 1] in key_matrix[1]:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[i]) + 1) % 5] + key_matrix[1][(key_matrix[1].index(plaintext[i + 1]) + 1) % 5]
        else:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[i]) + 1) % 5] + key_matrix[1][(key_matrix[1].index(plaintext[i + 1]) + 1) % 5]
    
    # If the plaintext has an odd number of characters, encrypt the last character alone
    if len(plaintext) % 2 == 1:
        if plaintext[-1] in key_matrix[0]:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[-1]) + 1) % 5]
        elif plaintext[-1] in key_matrix[1]:
            encrypted_text += key_matrix[1][(key_matrix[1].index(plaintext[-1]) + 1) % 5]
        else:
            encrypted_text += key_matrix[0][(key_matrix[0].index(plaintext[-1]) + 1) % 5]
    
    return encrypted_text.upper()

