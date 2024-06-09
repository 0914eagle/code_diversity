
def get_original_passwords(encrypted_password):
    # Initialize a list to store the original passwords
    original_passwords = []

    # Loop through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, double it and add an 'o' in between
        if encrypted_password[i].islower() and encrypted_password[i] != 'o':
            original_passwords.append(encrypted_password[:i] + encrypted_password[i] + 'o' + encrypted_password[i] + encrypted_password[i+1:])
        # If the current character is a vowel, just add it to the list
        else:
            original_passwords.append(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i+1:])

    # Return the number of original passwords
    return len(original_passwords) % 1000009

