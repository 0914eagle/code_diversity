
import re

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]{1,3}$"
    return re.search(regex, email) is not None

def get_valid_emails(emails):
    return list(filter(is_valid_email, emails))

def main():
    num_emails = int(input())
    emails = []
    for _ in range(num_emails):
        emails.append(input())
    valid_emails = get_valid_emails(emails)
    print(valid_emails)

if __name__ == '__main__':
    main()

