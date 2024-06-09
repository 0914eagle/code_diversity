
def f1(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_original_passwords = []
    
    # Iterate through the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, double it and add an 'o' in between
        if encrypted_password[i].lower() not in "aeiou":
            possible_original_passwords.append(encrypted_password[:i] + "o" + encrypted_password[i] + encrypted_password[i] + encrypted_password[i+1:])
        # If the current character is a vowel, just add it to the list
        else:
            possible_original_passwords.append(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i+1:])
    
    # Return the number of possible original passwords
    return len(possible_original_passwords) % 1000009

def f2(encrypted_password):
    # Initialize a set to store the possible original passwords
    possible_original_passwords = set()
    
    # Iterate through the encrypted password
    for i in range(len(encrypted_password)):
        # If the current character is a consonant, double it and add an 'o' in between
        if encrypted_password[i].lower() not in "aeiou":
            possible_original_passwords.add(encrypted_password[:i] + "o" + encrypted_password[i] + encrypted_password[i] + encrypted_password[i+1:])
        # If the current character is a vowel, just add it to the list
        else:
            possible_original_passwords.add(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i+1:])
    
    # Return the number of possible original passwords
    return len(possible_original_passwords) % 1000009

if __name__ == '__main__':
    encrypted_password = input()
    print(f1(encrypted_password))
    print(f2(encrypted_password))

