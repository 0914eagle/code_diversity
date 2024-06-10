
import re

def get_email_addresses(n):
    email_addresses = []
    for _ in range(n):
        email_addresses.append(input())
    return email_addresses

def is_valid_email_address(email_address):
    regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$"
    return re.search(regex, email_address) is not None

def filter_email_addresses(email_addresses):
    return list(filter(is_valid_email_address, email_addresses))

def sort_email_addresses(email_addresses):
    return sorted(email_addresses)

def main():
    n = int(input())
    email_addresses = get_email_addresses(n)
    valid_email_addresses = filter_email_addresses(email_addresses)
    sorted_email_addresses = sort_email_addresses(valid_email_addresses)
    print(sorted_email_addresses)

if __name__ == '__main__':
    main()

