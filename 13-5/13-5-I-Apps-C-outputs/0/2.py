
def f1(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_original_passwords = []
    
    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, check if the next character is also a consonant
        if encrypted_password[i].lower() in "bcdfghjklmnpqrstvwxyz":
            if i + 1 < len(encrypted_password) and encrypted_password[i + 1].lower() in "bcdfghjklmnpqrstvwxyz":
                # If the next character is also a consonant, add the current character and the next character to the list of possible original passwords
                possible_original_passwords.append(encrypted_password[i] + encrypted_password[i + 1])
            else:
                # If the next character is not a consonant, add the current character to the list of possible original passwords
                possible_original_passwords.append(encrypted_password[i])
        else:
            # If the current character is a vowel, add it to the list of possible original passwords
            possible_original_passwords.append(encrypted_password[i])
    
    # Return the number of possible original passwords
    return len(possible_original_passwords) % 1000009

def f2(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_original_passwords = []
    
    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, check if the next character is also a consonant
        if encrypted_password[i].lower() in "bcdfghjklmnpqrstvwxyz":
            if i + 1 < len(encrypted_password) and encrypted_password[i + 1].lower() in "bcdfghjklmnpqrstvwxyz":
                # If the next character is also a consonant, add the current character and the next character to the list of possible original passwords
                possible_original_passwords.append(encrypted_password[i] + encrypted_password[i + 1])
            else:
                # If the next character is not a consonant, add the current character to the list of possible original passwords
                possible_original_passwords.append(encrypted_password[i])
        else:
            # If the current character is a vowel, add it to the list of possible original passwords
            possible_original_passwords.append(encrypted_password[i])
    
    # Return the number of possible original passwords
    return len(possible_original_passwords) % 1000009

if __name__ == '__main__':
    encrypted_password = input()
    print(f1(encrypted_password))
    print(f2(encrypted_password))

