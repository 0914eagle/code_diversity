
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    key = []
    for char in key_phrase:
        if char != " " and char != "q":
            key.append(char)
    
    # Fill in the remaining letters of the alphabet
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in key:
            key.append(char)
    
    # Reshape the key into a 5x5 matrix
    key = [key[i:i+5] for i in range(0, len(key), 5)]
    
    # Encrypt the plaintext
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            # If there is only one letter left, add an 'X' after it
            ciphertext += key[0][key[0].index(plaintext[i])] + "X"
        else:
            # Apply the encryption rules
            if plaintext[i] == plaintext[i+1]:
                # If the letters are the same, add an 'X' after the first letter
                ciphertext += key[0][key[0].index(plaintext[i])] + "X"
            elif key[0].index(plaintext[i]) == key[0].index(plaintext[i+1]):
                # If the letters are in the same row, replace them with the letters to their immediate right
                ciphertext += key[0][(key[0].index(plaintext[i]) + 1) % 5] + key[0][(key[0].index(plaintext[i+1]) + 1) % 5]
            elif key[0].index(plaintext[i]) // 5 == key[0].index(plaintext[i+1]) // 5:
                # If the letters are in the same column, replace them with the letters immediately below
                ciphertext += key[(key[0].index(plaintext[i]) // 5 + 1) % 5][key[0].index(plaintext[i])] + key[(key[0].index(plaintext[i+1]) // 5 + 1) % 5][key[0].index(plaintext[i+1])]
            else:
                # If the letters are not in the same row or column, replace them with the letters on the same row but at the other pair of corners of the rectangle
                ciphertext += key[key[0].index(plaintext[i]) // 5][(key[0].index(plaintext[i]) + 1) % 5] + key[key[0].index(plaintext[i+1]) // 5][(key[0].index(plaintext[i+1]) + 1) % 5]
    
    return ciphertext.upper()

