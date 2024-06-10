
import re

def is_complex_enough(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=-]).{5,}$"
    return bool(re.search(pattern, password))

def main():
    password = input("Enter a password: ")
    if is_complex_enough(password):
        print("Correct")
    else:
        print("Too weak")

if __name__ == '__main__':
    main()

