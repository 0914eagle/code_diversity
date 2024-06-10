
import re

def extract_email_addresses(input_string):
    
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
    email_addresses = re.findall(email_regex, input_string)
    return email_addresses

def filter_email_addresses(email_addresses, min_length=0, max_length=100):
    
    filtered_email_addresses = []
    for email_address in email_addresses:
        if min_length <= len(email_address) <= max_length:
            filtered_email_addresses.append(email_address)
    return filtered_email_addresses

def sort_email_addresses(email_addresses):
    
    return sorted(email_addresses)

def main():
    num_email_addresses = int(input())
    email_addresses = []
    for _ in range(num_email_addresses):
        email_addresses.append(input())
    email_addresses = extract_email_addresses(" ".join(email_addresses))
    email_addresses = filter_email_addresses(email_addresses, 10, 30)
    email_addresses = sort_email_addresses(email_addresses)
    print(email_addresses)

if __name__ == "__main__":
    main()

