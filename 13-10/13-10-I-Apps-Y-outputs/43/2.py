
def create_table(key):
    table = []
    for i in range(5):
        table.append([])
    for i in range(len(key)):
        if key[i] != ' ' and key[i] != 'q':
            table[i % 5].append(key[i])
    for i in range(5):
        for j in range(5):
            if table[i][j] == None:
                table[i][j] = chr(ord('a') + (i * 5 + j) - (len(key) - 1))
    return table

def encrypt(table, plaintext):
    ciphertext = ''
    for i in range(0, len(plaintext) - 1, 2):
        if plaintext[i] == plaintext[i + 1]:
            ciphertext += table[ord(plaintext[i]) - ord('a')][0] + 'X'
        elif plaintext[i] in table[ord(plaintext[i + 1]) - ord('a')]:
            ciphertext += table[ord(plaintext[i]) - ord('a')][ord(plaintext[i + 1]) - ord('a') + 1]
        elif plaintext[i + 1] in table[ord(plaintext[i]) - ord('a')]:
            ciphertext += table[ord(plaintext[i + 1]) - ord('a')][ord(plaintext[i]) - ord('a')]
        else:
            for j in range(5):
                if table[j][0] == plaintext[i]:
                    ciphertext += table[j][ord(plaintext[i + 1]) - ord('a') + 1]
                if table[j][0] == plaintext[i + 1]:
                    ciphertext += table[j][ord(plaintext[i]) - ord('a')]
    if len(plaintext) % 2 == 1:
        ciphertext += table[ord(plaintext[-1]) - ord('a')][0]
    return ciphertext

def main():
    key = input()
    plaintext = input()
    table = create_table(key)
    ciphertext = encrypt(table, plaintext)
    print(ciphertext.upper())

if __name__ == '__main__':
    main()

