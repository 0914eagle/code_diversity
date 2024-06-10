
def generate_playfair_key(key_phrase):
    key_phrase = key_phrase.replace(" ", "")
    key_phrase = key_phrase.upper()
    key = ""
    for i in range(5):
        for j in range(5):
            if key_phrase[i * 5 + j] not in key:
                key += key_phrase[i * 5 + j]
            else:
                key += key[i * 5 + j]
    key += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return key

def encrypt_playfair(key, plaintext):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 == len(plaintext):
            ciphertext += key[key.find(plaintext[i])]
        elif plaintext[i] == plaintext[i + 1]:
            ciphertext += key[key.find(plaintext[i])] + "X"
        elif key[key.find(plaintext[i]) + 1] == plaintext[i + 1]:
            ciphertext += key[key.find(plaintext[i]) + 2]
        elif key[key.find(plaintext[i + 1]) + 1] == plaintext[i]:
            ciphertext += key[key.find(plaintext[i + 1]) + 2]
        elif key[key.find(plaintext[i]) // 5] == key[key.find(plaintext[i + 1]) // 5]:
            ciphertext += key[(key.find(plaintext[i]) + 1) % 25]
        else:
            ciphertext += key[(key.find(plaintext[i + 1]) + 1) % 25]
    return ciphertext

def main():
    key_phrase = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    key = generate_playfair_key(key_phrase)
    ciphertext = encrypt_playfair(key, plaintext)
    print(ciphertext)

if __name__ == '__main__':
    main()

