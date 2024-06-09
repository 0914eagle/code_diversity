
def check_password_complexity(password):
    # Initialize a flag to keep track of the password's complexity
    complex_enough = True

    # Check if the password is at least 5 characters long
    if len(password) < 5:
        complex_enough = False

    # Check if the password contains at least one large English letter
    if not any(c.isupper() for c in password):
        complex_enough = False

    # Check if the password contains at least one small English letter
    if not any(c.islower() for c in password):
        complex_enough = False

    # Check if the password contains at least one digit
    if not any(c.isdigit() for c in password):
        complex_enough = False

    # Return the result of the password's complexity check
    if complex_enough:
        return "Correct"
    else:
        return "Too weak"

if __name__ == '__main__':
    password = input("Enter a password: ")
    print(check_password_complexity(password))

