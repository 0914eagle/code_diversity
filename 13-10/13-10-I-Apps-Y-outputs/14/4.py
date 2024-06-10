
def get_number_of_groups(n):
    # Calculate the number of groups of three or more students
    num_groups = (n - 1) // 2
    return num_groups

def main():
    # Read the input
    n = int(input())

    # Call the function to get the number of groups
    num_groups = get_number_of_groups(n)

    # Print the result
    print(num_groups)

if __name__ == '__main__':
    main()

