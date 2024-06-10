
def get_encryption_key(key_phrase):
    # Initialize an empty 5x5 table
    table = [['' for _ in range(5)] for _ in range(5)]

    # Fill in the table with the key phrase
    for i, char in enumerate(key_phrase):
        if char != 'q':
            table[i // 5][i % 5] = char

    # Fill in the remaining cells with the rest of the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(25):
        if table[i // 5][i % 5] == '':
            table[i // 5][i % 5] = alphabet[i]

    return table

def encrypt_message(table, message):
    # Remove all spaces and duplicate letters from the message
    message = ''.join(set(message.lower()))

    # Break the message into digraphs
    digraphs = [message[i:i+2] for i in range(0, len(message), 2)]

    # Apply the encryption rules
    encrypted_digraphs = []
    for digraph in digraphs:
        if len(digraph) == 1:
            # If the digraph is a single letter, add an 'x' after it
            encrypted_digraphs.append(digraph + 'x')
        elif len(digraph) == 2:
            # If the digraph is a pair of letters, apply the encryption rules
            row1 = table.index(digraph[0]) // 5
            col1 = table.index(digraph[0]) % 5
            row2 = table.index(digraph[1]) // 5
            col2 = table.index(digraph[1]) % 5
            if row1 == row2:
                # If the letters are in the same row, replace them with the letters to their immediate right
                encrypted_digraphs.append(table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5])
            elif col1 == col2:
                # If the letters are in the same column, replace them with the letters immediately below
                encrypted_digraphs.append(table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2])
            else:
                # If the letters are not in the same row or column, replace them with the letters on the same row but at the other pair of corners of the rectangle
                encrypted_digraphs.append(table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5])

    # Join the encrypted digraphs into a single string
    return ''.join(encrypted_digraphs)

def main():
    key_phrase = input("Enter key phrase: ")
    message = input("Enter message to encrypt: ")
    table = get_encryption_key(key_phrase)
    encrypted_message = encrypt_message(table, message)
    print("Encrypted message:", encrypted_message)

if __name__ == '__main__':
    main()

