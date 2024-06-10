
def get_number_of_groups(n):
    # Find the closest number of groups that can be formed with 3 or more students
    num_groups = (n + 2) // 3
    return num_groups

def main():
    n = int(input())
    num_groups = get_number_of_groups(n)
    print(num_groups)

if __name__ == '__main__':
    main()

