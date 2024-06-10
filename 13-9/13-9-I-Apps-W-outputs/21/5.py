
import re

def check_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!?.,_])[A-Za-z0-9!?.,_]{5,}$"
    if re.match(pattern, password):
        return "Correct"
    else:
        return "Too weak"

def main():
    password = input("Enter password: ")
    print(check_password(password))

if __name__ == '__main__':
    main()

