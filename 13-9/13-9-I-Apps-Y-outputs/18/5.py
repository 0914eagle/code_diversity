
def is_password_valid(stored_password, entered_password):
    if stored_password == entered_password:
        return True
    
    # Check if entered password can be formed by prepending a single digit to the stored password
    if entered_password[1:] == stored_password:
        return True
    
    # Check if entered password can be formed by appending a single digit to the stored password
    if stored_password[1:] == entered_password:
        return True
    
    # Check if entered password is equal to the stored password after reversing the case of all letters
    if stored_password.lower() == entered_password.lower():
        return True
    
    return False

def main():
    stored_password = input("Enter the stored password: ")
    entered_password = input("Enter the entered password: ")
    if is_password_valid(stored_password, entered_password):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

