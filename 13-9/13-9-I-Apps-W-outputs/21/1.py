
def check_password_complexity(password):
    # Initialize a counter for the number of conditions met
    count = 0
    
    # Check if the password is at least 5 characters long
    if len(password) >= 5:
        count += 1
    
    # Check if the password contains at least one large English letter
    if any(c.isupper() for c in password):
        count += 1
    
    # Check if the password contains at least one small English letter
    if any(c.islower() for c in password):
        count += 1
    
    # Check if the password contains at least one digit
    if any(c.isdigit() for c in password):
        count += 1
    
    # Return "Correct" if the password meets all conditions, otherwise return "Too weak"
    if count == 4:
        return "Correct"
    else:
        return "Too weak"

def main():
    password = input("Enter a password: ")
    print(check_password_complexity(password))

if __name__ == '__main__':
    main()

