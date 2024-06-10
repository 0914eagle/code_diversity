
def get_login(first_name, last_name):
    # find the earliest possible login for the user
    login = first_name[0] + last_name[0]
    return login

def main():
    first_name, last_name = input().split()
    login = get_login(first_name, last_name)
    print(login)

if __name__ == '__main__':
    main()

