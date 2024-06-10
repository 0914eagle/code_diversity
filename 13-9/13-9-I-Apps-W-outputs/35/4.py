
def get_login(first_name, last_name):
    # find the earliest possible login for the given names
    return earliest_login(first_name, last_name)

def earliest_login(first_name, last_name):
    # find the earliest possible login for the given names
    return first_name[0] + last_name[0]

if __name__ == '__main__':
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    print(get_login(first_name, last_name))

