
def reverse_case(string):
    return string.swapcase()

def is_password_valid(stored_password, attempted_password):
    if stored_password == attempted_password:
        return True
    if attempted_password.startswith(stored_password):
        return True
    if attempted_password.endswith(stored_password):
        return True
    if reverse_case(attempted_password) == stored_password:
        return True
    return False

def main():
    stored_password = input("Enter the stored password: ")
    attempted_password = input("Enter the attempted password: ")
    if is_password_valid(stored_password, attempted_password):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

