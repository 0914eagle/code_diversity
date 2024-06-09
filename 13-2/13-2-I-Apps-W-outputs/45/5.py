
def get_min_passwords(passwords):
    # Initialize a set to store the equivalent passwords
    equivalent_passwords = set()

    # Iterate over the passwords
    for i in range(len(passwords)):
        for j in range(i+1, len(passwords)):
            # Check if the passwords are equivalent
            if are_equivalent(passwords[i], passwords[j]):
                # If they are equivalent, add them to the set of equivalent passwords
                equivalent_passwords.add(passwords[i])
                equivalent_passwords.add(passwords[j])

    # Return the length of the set of equivalent passwords
    return len(equivalent_passwords)

def are_equivalent(password1, password2):
    # Check if the passwords have any common letters
    for letter in password1:
        if letter in password2:
            return True
    return False

n = int(input())
passwords = []

# Read the passwords from the input
for i in range(n):
    passwords.append(input())

# Call the function to get the minimal number of passwords
result = get_min_passwords(passwords)

# Print the result
print(result)

