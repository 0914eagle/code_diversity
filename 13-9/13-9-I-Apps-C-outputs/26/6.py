
def count_possible_passwords(encrypted_password):
    # Initialize a list to store the possible passwords
    possible_passwords = []
    
    # Iterate through the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, double it and add an 'o' in between
        if encrypted_password[i].lower() not in "aeiou":
            possible_passwords.append(encrypted_password[:i] + "o" + encrypted_password[i] + encrypted_password[i] + encrypted_password[i+1:])
        # If the current character is a vowel, just add it to the list
        else:
            possible_passwords.append(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i+1:])
    
    # Return the number of possible passwords modulo 1000009
    return len(possible_passwords) % 1000009

