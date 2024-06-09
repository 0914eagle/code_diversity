
def playfair_cipher(key_phrase, plaintext):
    # Create the encryption key
    key = [char for char in key_phrase if char != ' ']
    key += [char for char in 'abcdefghijklmnopqrstuvwxyz' if char not in key]
    key = ''.join(key)
    
    # Create the encryption table
    table = [key[i:i+5] for i in range(0, len(key), 5)]
    
    # Encrypt the plaintext
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        if plaintext[i] == plaintext[i+1]:
            ciphertext += plaintext[i] + 'X'
        elif plaintext[i] in table[0]:
            ciphertext += table[0][table[0].index(plaintext[i])+1]
        elif plaintext[i+1] in table[0]:
            ciphertext += table[0][table[0].index(plaintext[i+1])+1]
        elif plaintext[i] in table[1]:
            ciphertext += table[1][table[1].index(plaintext[i])+1]
        elif plaintext[i+1] in table[1]:
            ciphertext += table[1][table[1].index(plaintext[i+1])+1]
        elif plaintext[i] in table[2]:
            ciphertext += table[2][table[2].index(plaintext[i])+1]
        elif plaintext[i+1] in table[2]:
            ciphertext += table[2][table[2].index(plaintext[i+1])+1]
        elif plaintext[i] in table[3]:
            ciphertext += table[3][table[3].index(plaintext[i])+1]
        elif plaintext[i+1] in table[3]:
            ciphertext += table[3][table[3].index(plaintext[i+1])+1]
        elif plaintext[i] in table[4]:
            ciphertext += table[4][table[4].index(plaintext[i])+1]
        elif plaintext[i+1] in table[4]:
            ciphertext += table[4][table[4].index(plaintext[i+1])+1]
    
    return ciphertext.upper()

