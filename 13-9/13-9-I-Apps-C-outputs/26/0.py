
def get_possible_passwords(encrypted_password):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    possible_passwords = 0
    for i in range(len(encrypted_password)):
        if encrypted_password[i] in vowels:
            possible_passwords += 1
        elif encrypted_password[i] in consonants:
            possible_passwords += 2
    return possible_passwords % 1000009

