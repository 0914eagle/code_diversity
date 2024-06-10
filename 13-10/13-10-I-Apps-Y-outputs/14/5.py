
def get_number_of_groups(n):
    # Find the closest number of groups that consist of three or more students
    return (n + 2) // 3

def main():
    n = int(input())
    print(get_number_of_groups(n))

if __name__ == '__main__':
    main()

