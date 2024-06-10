
def is_acceptable_password(stored_password, attempted_password):
    # Check if the stored and attempted passwords are identical
    if stored_password == attempted_password:
        return True

    # Check if the stored password can be formed from the attempted password by prepending a single digit
    if len(attempted_password) > 1 and stored_password.startswith(attempted_password[1:]):
        return True

    # Check if the stored password can be formed from the attempted password by appending a single digit
    if len(attempted_password) > 1 and stored_password.endswith(attempted_password[:-1]):
        return True

    # Check if the stored password is equal to the attempted password after reversing the case of all letters in the attempted password
    if stored_password == attempted_password[::-1]:
        return True

    # If none of the above conditions are met, return False
    return False

def main():
    stored_password = input("Enter the stored password: ")
    attempted_password = input("Enter the attempted password: ")
    if is_acceptable_password(stored_password, attempted_password):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

