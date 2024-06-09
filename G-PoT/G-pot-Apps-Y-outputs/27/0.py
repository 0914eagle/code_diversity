
encrypted_message = input().strip()
key = input().strip()

decrypted_message = ""
for i in range(len(encrypted_message)):
    shift = ord(key[i]) - ord('A')
    if i % 2 == 0:
        decrypted_char = chr((ord(encrypted_message[i]) - shift - ord('A')) % 26 + ord('A'))
    else:
        decrypted_char = chr((ord(encrypted_message[i]) + shift - ord('A')) % 26 + ord('A'))
    decrypted_message += decrypted_char

print(decrypted_message)
