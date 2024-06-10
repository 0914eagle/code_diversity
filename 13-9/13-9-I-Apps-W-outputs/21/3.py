
def check_password_complexity(password):
    # Check if the password is at least 5 characters long
    if len(password) < 5:
        return "Too weak"
    
    # Check if the password contains at least one large English letter
    if not any(c.isupper() for c in password):
        return "Too weak"
    
    # Check if the password contains at least one small English letter
    if not any(c.islower() for c in password):
        return "Too weak"
    
    # Check if the password contains at least one digit
    if not any(c.isdigit() for c in password):
        return "Too weak"
    
    # If all conditions are met, return "Correct"
    return "Correct"

def main():
    password = input("Enter a password: ")
    print(check_password_complexity(password))

if __name__ == '__main__':
    main()

