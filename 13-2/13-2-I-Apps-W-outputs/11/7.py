
def check_password_complexity(password):
    # Initialize a counter for the number of conditions met
    conditions_met = 0

    # Check if the password is at least 5 characters long
    if len(password) >= 5:
        conditions_met += 1

    # Check if the password contains at least one large English letter
    if any(c.isupper() for c in password):
        conditions_met += 1

    # Check if the password contains at least one small English letter
    if any(c.islower() for c in password):
        conditions_met += 1

    # Check if the password contains at least one digit
    if any(c.isdigit() for c in password):
        conditions_met += 1

    # Return "Correct" if all conditions are met, otherwise return "Too weak"
    if conditions_met == 4:
        return "Correct"
    else:
        return "Too weak"

if __name__ == '__main__':
    password = input("Enter a password: ")
    print(check_password_complexity(password))

