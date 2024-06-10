
def get_login(first_name, last_name):
    logins = []
    for i in range(1, len(first_name) + 1):
        for j in range(1, len(last_name) + 1):
            logins.append(first_name[:i] + last_name[:j])
    return sorted(logins)[0]

def main():
    first_name, last_name = input("Enter first and last name: ").strip().split()
    print(get_login(first_name, last_name))

if __name__ == '__main__':
    main()

