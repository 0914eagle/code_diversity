
def get_min_passwords(passwords):
    # Initialize a set to store the equivalent passwords
    equivalent_passwords = set()

    # Iterate over the passwords
    for i in range(len(passwords)):
        for j in range(i+1, len(passwords)):
            # Check if the passwords are equivalent
            if are_equivalent(passwords[i], passwords[j]):
                # Add the passwords to the set of equivalent passwords
                equivalent_passwords.add(passwords[i])
                equivalent_passwords.add(passwords[j])

    # Return the length of the set of equivalent passwords
    return len(equivalent_passwords)

def are_equivalent(password1, password2):
    # Check if the passwords have any common letters
    for letter in password1:
        if letter in password2:
            return True

    # Check if there is a password in the list that is equivalent to both passwords
    for password in passwords:
        if are_equivalent(password, password1) and are_equivalent(password, password2):
            return True

    # If none of the above conditions are met, the passwords are not equivalent
    return False

# Test the function with the example input
passwords = ["a", "b", "ab", "d"]
print(get_min_passwords(passwords))

# Test the function with another example input
passwords = ["ab", "bc", "abc"]
print(get_min_passwords(passwords))

# Test the function with a third example input
passwords = ["codeforces"]
print(get_min_passwords(passwords))

