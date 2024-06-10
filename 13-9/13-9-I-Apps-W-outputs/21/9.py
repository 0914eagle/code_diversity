
import re

def is_complex_enough(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(.{5,})$"
    return bool(re.match(pattern, password))

def check_password(password):
    if is_complex_enough(password):
        return "Correct"
    else:
        return "Too weak"

if __name__ == '__main__':
    password = input("Enter your password: ")
    print(check_password(password))

