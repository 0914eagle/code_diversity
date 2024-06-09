
def f1(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_passwords = []
    
    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, check if the next character is also a consonant
        if encrypted_password[i].isalpha() and encrypted_password[i].islower() and encrypted_password[i+1].isalpha() and encrypted_password[i+1].islower():
            # If the next character is also a consonant, add the possible original password to the list
            possible_passwords.append(encrypted_password[:i] + encrypted_password[i:i+2] + encrypted_password[i+2:])
    
    # Return the number of possible original passwords
    return len(possible_passwords) % 1000009

