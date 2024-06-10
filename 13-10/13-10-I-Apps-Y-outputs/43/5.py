
def playfair_cipher(key, plaintext):
    # Create the encryption key
    key = key.replace(" ", "")
    key = key.upper()
    key = key.replace("Q", "")
    key_list = list(key)
    key_list = list(dict.fromkeys(key_list))
    key_list.sort()
    key_list.append("X")
    
    # Create the encryption table
    table = [[""] * 5 for _ in range(5)]
    for i in range(len(key_list)):
        table[i // 5][i % 5] = key_list[i]
    
    # Encrypt the plaintext
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            ciphertext += table[plaintext[i]][0]
        else:
            if plaintext[i] == plaintext[i + 1]:
                ciphertext += table[plaintext[i]][0] + "X"
            elif table[plaintext[i]][plaintext[i + 1]].isalpha():
                ciphertext += table[plaintext[i]][plaintext[i + 1]]
            elif table[plaintext[i + 1]][plaintext[i]].isalpha():
                ciphertext += table[plaintext[i + 1]][plaintext[i]]
            else:
                ciphertext += table[plaintext[i]][table[plaintext[i + 1]].index(plaintext[i])]
    
    return ciphertext

def main():
    key = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    ciphertext = playfair_cipher(key, plaintext)
    print(ciphertext)

if __name__ == '__main__':
    main()

