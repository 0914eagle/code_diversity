
def check_password(stored_password, attempted_password):
    # Check if the stored and attempted passwords are identical
    if stored_password == attempted_password:
        return True

    # Check if the attempted password can be formed by prepending a single digit to the stored password
    if len(attempted_password) == len(stored_password) + 1 and attempted_password[1:] == stored_password:
        return True

    # Check if the attempted password can be formed by appending a single digit to the stored password
    if len(attempted_password) == len(stored_password) + 1 and attempted_password[:-1] == stored_password:
        return True

    # Check if the attempted password is equal to the stored password after reversing the case of all letters
    if stored_password.lower() == attempted_password.lower():
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

