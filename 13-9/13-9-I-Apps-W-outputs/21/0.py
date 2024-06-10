
def check_password(password):
    # Your code here
    return "Correct" if len(password) >= 5 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) else "Too weak"

def main():
    password = input("Enter password: ")
    print(check_password(password))

if __name__ == '__main__':
    main()

