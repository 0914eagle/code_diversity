
import re

def is_valid_email(email):
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.search(regex, email) is not None

def get_valid_emails(emails):
    return list(filter(is_valid_email, emails))

def sort_emails(emails):
    return sorted(emails)

def main():
    num_emails = int(input())
    emails = []
    for _ in range(num_emails):
        emails.append(input())
    valid_emails = get_valid_emails(emails)
    sorted_emails = sort_emails(valid_emails)
    print(sorted_emails)

if __name__ == '__main__':
    main()

