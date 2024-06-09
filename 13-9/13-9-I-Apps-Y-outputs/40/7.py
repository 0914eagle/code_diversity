
def playfair_cipher(key_phrase, plaintext):
    # Initialize the encryption key
    encryption_key = ""
    for char in key_phrase:
        if char != " " and char not in encryption_key:
            encryption_key += char
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in encryption_key:
            encryption_key += char
    
    # Remove spaces and duplicate letters from the plaintext
    plaintext = plaintext.replace(" ", "")
    plaintext = "".join(set(plaintext))
    
    # Encrypt the plaintext
    encrypted_text = ""
    for i in range(0, len(plaintext), 2):
        if i + 1 == len(plaintext):
            encrypted_text += encryption_key[ord(plaintext[i]) - ord("a")]
        else:
            first_char = plaintext[i]
            second_char = plaintext[i + 1]
            if first_char == second_char:
                first_char = encryption_key[ord(first_char) - ord("a") + 1]
                second_char = encryption_key[ord(second_char) - ord("a") + 1]
            elif first_char == "x":
                first_char = encryption_key[ord(second_char) - ord("a") - 1]
            elif second_char == "x":
                second_char = encryption_key[ord(first_char) - ord("a") - 1]
            else:
                first_char = encryption_key[ord(first_char) - ord("a")]
                second_char = encryption_key[ord(second_char) - ord("a")]
            encrypted_text += first_char + second_char
    
    return encrypted_text.upper()

