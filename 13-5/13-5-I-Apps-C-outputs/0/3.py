
def f1(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_passwords = []
    
    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, check if the previous character is also a consonant
        if encrypted_password[i].isalpha() and encrypted_password[i].islower() and encrypted_password[i-1].isalpha() and encrypted_password[i-1].islower():
            # If the previous character is also a consonant, add the current character to the list of possible original passwords
            possible_passwords.append(encrypted_password[i])
    
    # Return the number of possible original passwords
    return len(possible_passwords)

def f2(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_passwords = []
    
    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, check if the previous character is also a consonant
        if encrypted_password[i].isalpha() and encrypted_password[i].islower() and encrypted_password[i-1].isalpha() and encrypted_password[i-1].islower():
            # If the previous character is also a consonant, add the current character to the list of possible original passwords
            possible_passwords.append(encrypted_password[i])
    
    # Return the number of possible original passwords
    return len(possible_passwords)

if __name__ == '__main__':
    encrypted_password = input()
    print(f1(encrypted_password))
    print(f2(encrypted_password))

