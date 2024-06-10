
def get_playfair_key(key_phrase):
    key_phrase = key_phrase.replace(" ", "").upper()
    key_table = []
    for i in range(5):
        for j in range(5):
            if len(key_phrase) == 0:
                break
            key_table.append(key_phrase[0])
            key_phrase = key_phrase[1:]
    for i in range(5):
        for j in range(5):
            if key_table[i*5+j] == "Q":
                key_table[i*5+j] = "Z"
    return "".join(key_table)

def encrypt_playfair(key, plaintext):
    key = key.upper()
    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            ciphertext += key[key.find(plaintext[i])] + "X"
            break
        pair = plaintext[i:i+2]
        if pair[0] == pair[1]:
            ciphertext += key[key.find(pair[0])] + "X"
        elif key.find(pair[0]) == key.find(pair[1]):
            ciphertext += key[key.find(pair[0])+1] + key[key.find(pair[1])+1]
        elif key[key.find(pair[0])] == key[key.find(pair[1])]:
            ciphertext += key[key.find(pair[0])+5] + key[key.find(pair[1])+5]
        else:
            ciphertext += key[key.find(pair[0])+1] + key[key.find(pair[1])+1]
    return ciphertext

def main():
    key_phrase = input("Enter key phrase: ")
    plaintext = input("Enter plaintext: ")
    key = get_playfair_key(key_phrase)
    ciphertext = encrypt_playfair(key, plaintext)
    print("Ciphertext:", ciphertext)

if __name__ == '__main__':
    main()

