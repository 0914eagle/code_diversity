
def f1(encrypted_password):
    # Initialize a dictionary to store the number of ways each letter can be transformed
    letter_transforms = {}
    for letter in encrypted_password:
        if letter.isalpha():
            if letter.islower():
                # If the letter is a lowercase letter, it can be transformed into two letters
                letter_transforms[letter] = 2
            else:
                # If the letter is an uppercase letter, it can be transformed into three letters
                letter_transforms[letter] = 3
        else:
            # If the letter is not a letter, it can be transformed into one letter
            letter_transforms[letter] = 1
    
    # Initialize a variable to store the total number of ways the password can be transformed
    total_transforms = 1
    
    # Iterate through the dictionary of letter transforms and multiply the total number of ways by the number of ways each letter can be transformed
    for letter, num_transforms in letter_transforms.items():
        total_transforms *= num_transforms
    
    # Return the total number of ways the password can be transformed
    return total_transforms % 1000009

def f2(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_passwords = []
    
    # Iterate through the encrypted password and check if each letter can be transformed
    for i in range(len(encrypted_password)):
        # If the letter is a lowercase letter, it can be transformed into two letters
        if encrypted_password[i].islower():
            possible_passwords.append(encrypted_password[:i] + "o" + encrypted_password[i] + "o" + encrypted_password[i+1:])
        # If the letter is an uppercase letter, it can be transformed into three letters
        else:
            possible_passwords.append(encrypted_password[:i] + "O" + encrypted_password[i] + "O" + encrypted_password[i+1:])
    
    # Return the list of possible original passwords
    return possible_passwords

if __name__ == '__main__':
    encrypted_password = input("Enter the encrypted password: ")
    print(f"The number of ways the password might have looked before Edvin translated it is {f1(encrypted_password)}")
    print(f"The possible original passwords are {f2(encrypted_password)}")

