
def get_login(first_name, last_name):
    return get_earliest_login(first_name, last_name)

def get_earliest_login(first_name, last_name):
    logins = []
    for i in range(1, len(first_name) + 1):
        for j in range(1, len(last_name) + 1):
            logins.append(first_name[:i] + last_name[:j])
    return sorted(logins)[0]

def get_input():
    first_name, last_name = input().strip().split()
    return first_name, last_name

if __name__ == '__main__':
    first_name, last_name = get_input()
    print(get_login(first_name, last_name))

