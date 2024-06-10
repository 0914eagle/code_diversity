
def get_key_phrase():
    key_phrase = input("Enter key phrase: ")
    return key_phrase

def get_plaintext():
    plaintext = input("Enter plaintext: ")
    return plaintext

def encrypt(key_phrase, plaintext):
    key_phrase = key_phrase.replace(" ", "")
    plaintext = plaintext.replace(" ", "")
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            encrypted_text += plaintext[i] + "x"
        elif plaintext[i] in "aeiou":
            encrypted_text += chr((ord(plaintext[i]) + 13) % 26 + 97)
        elif plaintext[i + 1] in "aeiou":
            encrypted_text += chr((ord(plaintext[i + 1]) + 13) % 26 + 97)
        else:
            encrypted_text += plaintext[i] + plaintext[i + 1]
    return encrypted_text.upper()

def main():
    key_phrase = get_key_phrase()
    plaintext = get_plaintext()
    encrypted_text = encrypt(key_phrase, plaintext)
    print(encrypted_text)

if __name__ == '__main__':
    main()

