
def get_earliest_login(first_name, last_name):
    # generate all possible logins for the given names
    logins = []
    for i in range(1, len(first_name) + 1):
        for j in range(1, len(last_name) + 1):
            logins.append(first_name[:i] + last_name[:j])
    
    # sort the logins alphabetically
    logins.sort()
    
    # return the earliest login
    return logins[0]

def main():
    first_name, last_name = input().split()
    print(get_earliest_login(first_name, last_name))

if __name__ == '__main__':
    main()

