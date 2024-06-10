
def get_login(first_name, last_name):
    # find the earliest login for the given first and last names
    return earliest_login(first_name, last_name)

def earliest_login(first_name, last_name):
    # initialize the earliest login as the empty string
    earliest = ""
    # iterate over the possible logins
    for i in range(len(first_name)):
        for j in range(len(last_name)):
            # form the current login
            login = first_name[:i+1] + last_name[:j+1]
            # check if the current login is earlier than the earliest login so far
            if login < earliest or earliest == "":
                # if so, update the earliest login
                earliest = login
    # return the earliest login
    return earliest

if __name__ == '__main__':
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(get_login(first_name, last_name))

