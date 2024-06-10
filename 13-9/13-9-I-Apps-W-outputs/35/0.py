
def get_earliest_login(first_name, last_name):
    # Find the earliest login by concatenating the first name and last name prefixes
    first_name_prefix = first_name[0]
    last_name_prefix = last_name[0]
    earliest_login = first_name_prefix + last_name_prefix
    
    # If the first name prefix is the same as the last name prefix, return the earliest login
    if first_name_prefix == last_name_prefix:
        return earliest_login
    
    # If the first name prefix is earlier alphabetically than the last name prefix, return the earliest login
    if first_name_prefix < last_name_prefix:
        return earliest_login
    
    # If the first name prefix is later alphabetically than the last name prefix, return the earliest login with the last name prefix instead of the first name prefix
    return last_name_prefix + first_name_prefix

def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(get_earliest_login(first_name, last_name))

if __name__ == '__main__':
    main()

