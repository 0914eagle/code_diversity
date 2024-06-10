
def get_login(first_name, last_name):
    
    first_prefix = get_prefix(first_name)
    last_prefix = get_prefix(last_name)
    return first_prefix + last_prefix

def get_prefix(name):
    
    return name[:1]

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    print(get_login(first_name, last_name))

if __name__ == '__main__':
    main()

