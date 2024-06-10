
import re

def create_key_table(key_phrase):
    key_phrase = re.sub(' +', '', key_phrase)
    key_table = [[' ' for _ in range(5)] for _ in range(5)]
    for i, char in enumerate(key_phrase):
        key_table[i % 5][i // 5] = char
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == ' ':
                key_table[i][j] = chr(ord('a') + (i * 5 + j) - 13)
    return key_table

def encrypt_message(key_table, message):
    message = re.sub(' +', '', message).upper()
    encrypted_message = ''
    for i in range(0, len(message), 2):
        if i == len(message) - 1:
            encrypted_message += key_table[0][0]
        elif message[i] == message[i + 1]:
            encrypted_message += key_table[0][0] + 'X'
        elif message[i] in key_table[0]:
            encrypted_message += key_table[0][key_table[0].index(message[i + 1])]
        elif message[i + 1] in key_table[0]:
            encrypted_message += key_table[0][key_table[0].index(message[i])]
        else:
            encrypted_message += key_table[key_table[0].index(message[i])][key_table[0].index(message[i + 1])]
    return encrypted_message

def main():
    key_phrase = input()
    message = input()
    key_table = create_key_table(key_phrase)
    encrypted_message = encrypt_message(key_table, message)
    print(encrypted_message)

if __name__ == '__main__':
    main()

