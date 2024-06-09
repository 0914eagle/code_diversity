
def playfair_cipher(key_phrase, plaintext):
    # Create a 5x5 table with the key phrase and the rest of the alphabet
    table = []
    for i in range(5):
        table.append(list(key_phrase[i::5]))
    for i in range(5):
        for j in range(5):
            if table[i][j] == ' ':
                table[i][j] = chr(ord('a') + i * 5 + j)
    
    # Encrypt the plaintext
    encrypted_text = ''
    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            encrypted_text += plaintext[i] + 'x'
        elif plaintext[i] in table[0]:
            row = table[0].index(plaintext[i])
            col = table[0].index(plaintext[i + 1])
            encrypted_text += table[row][(col + 1) % 5] + table[row][(col + 2) % 5]
        elif plaintext[i + 1] in table[0]:
            row = table[0].index(plaintext[i + 1])
            col = table[0].index(plaintext[i])
            encrypted_text += table[row][(col + 1) % 5] + table[row][(col + 2) % 5]
        else:
            row1 = table[0].index(plaintext[i])
            col1 = table[0].index(plaintext[i + 1])
            row2 = (row1 + 1) % 5
            col2 = (col1 + 1) % 5
            encrypted_text += table[row1][col2] + table[row2][col1]
    
    # If the plaintext has an odd number of characters, encrypt the last character
    if len(plaintext) % 2 == 1:
        if plaintext[-1] == plaintext[-2]:
            encrypted_text += plaintext[-1] + 'x'
        elif plaintext[-1] in table[0]:
            row = table[0].index(plaintext[-1])
            col = table[0].index(plaintext[-2])
            encrypted_text += table[row][(col + 1) % 5] + table[row][(col + 2) % 5]
        elif plaintext[-2] in table[0]:
            row = table[0].index(plaintext[-2])
            col = table[0].index(plaintext[-1])
            encrypted_text += table[row][(col + 1) % 5] + table[row][(col + 2) % 5]
        else:
            row1 = table[0].index(plaintext[-1])
            col1 = table[0].index(plaintext[-2])
            row2 = (row1 + 1) % 5
            col2 = (col1 + 1) % 5
            encrypted_text += table[row1][col2] + table[row2][col1]
    
    return encrypted_text.upper()

