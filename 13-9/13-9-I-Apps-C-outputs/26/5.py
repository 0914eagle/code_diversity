
def solve(encrypted_password):
    # Initialize a variable to store the number of possible original passwords
    num_possible_passwords = 0

    # Iterate through each possible original password
    for original_password in generate_possible_passwords(encrypted_password):
        # Check if the original password matches the encrypted password
        if is_match(original_password, encrypted_password):
            # Increment the number of possible original passwords
            num_possible_passwords += 1

    # Return the number of possible original passwords
    return num_possible_passwords % 1000009

def generate_possible_passwords(encrypted_password):
    # Initialize a list to store the possible original passwords
    possible_passwords = []

    # Iterate through each character in the encrypted password
    for i in range(len(encrypted_password)):
        # Check if the current character is a consonant
        if encrypted_password[i].lower() not in "aeiou":
            # Generate all possible original passwords with the current character doubled
            for possible_password in generate_possible_passwords(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i] + encrypted_password[i+1:]):
                # Add the possible original password to the list
                possible_passwords.append(possible_password)
        else:
            # Generate all possible original passwords with the current character unchanged
            for possible_password in generate_possible_passwords(encrypted_password[:i] + encrypted_password[i] + encrypted_password[i+1:]):
                # Add the possible original password to the list
                possible_passwords.append(possible_password)

    # If the list of possible original passwords is empty, return the empty string
    if not possible_passwords:
        possible_passwords.append("")

    # Return the list of possible original passwords
    return possible_passwords

def is_match(original_password, encrypted_password):
    # Initialize a variable to store the current index in the encrypted password
    i = 0

    # Iterate through each character in the original password
    for c in original_password:
        # Check if the current character is a consonant
        if c.lower() not in "aeiou":
            # Check if the next two characters in the encrypted password match the current character doubled
            if encrypted_password[i:i+2] != c + c:
                # If the characters do not match, return False
                return False
            # Increment the index in the encrypted password by 2
            i += 2
        else:
            # Check if the current character matches the next character in the encrypted password
            if encrypted_password[i] != c:
                # If the characters do not match, return False
                return False
            # Increment the index in the encrypted password by 1
            i += 1

    # If the entire original password has been processed, return True
    return True

