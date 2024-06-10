
def check_password(stored_password, attempted_password):
    # Convert both passwords to lowercase
    stored_password = stored_password.lower()
    attempted_password = attempted_password.lower()
    
    # Check if the passwords are identical
    if stored_password == attempted_password:
        return True
    
    # Check if the attempted password can be formed by prepending a single digit
    if attempted_password[1:] == stored_password:
        return True
    
    # Check if the attempted password can be formed by appending a single digit
    if stored_password[1:] == attempted_password:
        return True
    
    # Check if the attempted password is equal to the stored password after reversing the case of all letters
    if stored_password == attempted_password[::-1]:
        return True
    
    # If none of the above conditions are met, return False
    return False

def main():
    stored_password = input("Enter the stored password: ")
    attempted_password = input("Enter the attempted password: ")
    if check_password(stored_password, attempted_password):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

