
def check_password(stored_password, attempted_password):
    if stored_password == attempted_password:
        return True
    elif stored_password.startswith(attempted_password):
        return True
    elif stored_password.endswith(attempted_password):
        return True
    elif stored_password.lower() == attempted_password.lower():
        return True
    else:
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

