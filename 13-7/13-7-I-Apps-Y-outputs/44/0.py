
import re

def get_emails(n):
    emails = []
    for _ in range(n):
        emails.append(input())
    return emails

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
    return re.search(regex, email) is not None

def get_valid_emails(emails):
    return list(filter(is_valid_email, emails))

def sort_emails(emails):
    return sorted(emails)

def main():
    n = int(input())
    emails = get_emails(n)
    valid_emails = get_valid_emails(emails)
    sorted_emails = sort_emails(valid_emails)
    print(sorted_emails)

if __name__ == '__main__':
    main()

