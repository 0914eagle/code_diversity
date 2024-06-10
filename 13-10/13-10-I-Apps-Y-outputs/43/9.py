
def encrypt(key_phrase, plaintext):
    # Create a dictionary to map each letter to its position in the key phrase
    letter_map = {}
    for i, letter in enumerate(key_phrase):
        letter_map[letter] = i
    
    # Create a list of letters to use in the encryption
    letters = [letter for letter in key_phrase if letter != 'q']
    letters += [letter for letter in 'abcdefghijklmnoprstuvwxyz' if letter not in letters]
    
    # Encrypt the plaintext
    encrypted_text = ''
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            encrypted_text += 'X'
            break
        else:
            digraph = plaintext[i:i+2]
            if digraph[0] == digraph[1]:
                encrypted_text += 'X' + digraph[0]
            elif digraph[0] in letters[0:5] and digraph[1] in letters[0:5]:
                encrypted_text += letters[(letters.index(digraph[0]) + 1) % 5] + letters[(letters.index(digraph[1]) + 1) % 5]
            elif digraph[0] in letters[5:10] and digraph[1] in letters[5:10]:
                encrypted_text += letters[(letters.index(digraph[0]) - 5 + 1) % 5 + 5] + letters[(letters.index(digraph[1]) - 5 + 1) % 5 + 5]
            elif digraph[0] in letters[10:15] and digraph[1] in letters[10:15]:
                encrypted_text += letters[(letters.index(digraph[0]) - 10 + 1) % 5 + 10] + letters[(letters.index(digraph[1]) - 10 + 1) % 5 + 10]
            elif digraph[0] in letters[15:20] and digraph[1] in letters[15:20]:
                encrypted_text += letters[(letters.index(digraph[0]) - 15 + 1) % 5 + 15] + letters[(letters.index(digraph[1]) - 15 + 1) % 5 + 15]
    
    return encrypted_text.upper()

def main():
    key_phrase = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    encrypted_text = encrypt(key_phrase, plaintext)
    print(f"Encrypted text: {encrypted_text}")

if __name__ == '__main__':
    main()

