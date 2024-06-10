
def get_earliest_login(first_name, last_name):
    prefix_first_name = first_name[0]
    prefix_last_name = last_name[0]
    return min(prefix_first_name + prefix_last_name, prefix_last_name + prefix_first_name, key=lambda x: x.lower())

def main():
    first_name, last_name = input().split()
    print(get_earliest_login(first_name, last_name))

if __name__ == '__main__':
    main()

