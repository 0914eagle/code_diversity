
def create_key(key_phrase):
    key_phrase = key_phrase.upper()
    key_phrase = key_phrase.replace(" ", "")
    key_phrase = key_phrase.replace("Q", "")
    key = []
    for i in range(len(key_phrase)):
        if key_phrase[i] not in key:
            key.append(key_phrase[i])
    for i in range(len(key)):
        if len(key) < 25:
            key.append(chr(ord(key[i]) + 1))
    return "".join(key)

def encrypt(key, plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            ciphertext += key[ord(plaintext[i]) - 65]
        elif plaintext[i] == plaintext[i + 1]:
            ciphertext += key[ord(plaintext[i]) - 65] + "X"
        elif key.find(plaintext[i] + plaintext[i + 1]) != -1:
            ciphertext += key[key.find(plaintext[i] + plaintext[i + 1]) + 1]
        else:
            ciphertext += key[key.find(plaintext[i + 1] + plaintext[i]) - 1]
    return ciphertext

def main():
    key_phrase = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    key = create_key(key_phrase)
    ciphertext = encrypt(key, plaintext)
    print("Encrypted text:", ciphertext)

if __name__ == '__main__':
    main()

