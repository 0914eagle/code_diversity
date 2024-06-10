
def reverse_case(s):
    return s.swapcase()

def check_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return True
    if attempted_password.startswith(stored_password):
        return True
    if stored_password.startswith(attempted_password):
        return True
    if reverse_case(stored_password) == attempted_password:
        return True
    return False

def main():
    stored_password = input("Enter stored password: ")
    attempted_password = input("Enter attempted password: ")
    if check_password(stored_password, attempted_password):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

