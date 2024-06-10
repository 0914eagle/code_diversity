
def get_login(first_name, last_name):
    
    return first_name[0] + last_name[0]

def get_input():
    
    return input().split()

def main():
    first_name, last_name = get_input()
    login = get_login(first_name, last_name)
    print(login)

if __name__ == '__main__':
    main()

