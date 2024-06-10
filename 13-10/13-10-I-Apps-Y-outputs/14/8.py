
def get_number_of_groups(n):
    # Initialize a list to store the number of groups for each number of students
    num_groups = [0] * (n + 1)
    
    # Loop through each number of students and calculate the number of groups for that number of students
    for i in range(3, n + 1):
        num_groups[i] = num_groups[i - 1] + 1
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                num_groups[i] = max(num_groups[i], num_groups[i - j] + 1)
    
    # Return the maximum number of groups for the given number of students
    return max(num_groups)

def main():
    n = int(input())
    print(get_number_of_groups(n))

if __name__ == '__main__':
    main()

