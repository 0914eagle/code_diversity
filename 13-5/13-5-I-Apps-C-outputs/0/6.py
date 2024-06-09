
def f1(encrypted_password):
    # Initialize variables
    original_passwords = set()
    current_password = ""
    i = 0
    
    # Iterate through the encrypted password
    while i < len(encrypted_password):
        # If the current character is a consonant, double it and add an 'o' in between
        if encrypted_password[i].lower() not in "aeiou":
            current_password += encrypted_password[i] + "o" + encrypted_password[i]
        # If the current character is a vowel, add it to the current password
        else:
            current_password += encrypted_password[i]
        i += 1
    
    # Add the current password to the set of original passwords
    original_passwords.add(current_password)
    
    # Return the number of original passwords
    return len(original_passwords) % 1000009

