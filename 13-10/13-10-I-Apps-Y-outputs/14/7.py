
def group_students(n):
    # Initialize a list to store the groups
    groups = []
    
    # Iterate from 3 to n
    for i in range(3, n + 1):
        # Check if the number of students is divisible by i
        if n % i == 0:
            # Add the group to the list
            groups.append(i)
    
    # Return the length of the list, which is the maximum number of groups consisting of three or more students
    return len(groups)

def main():
    # Read the number of students from stdin
    n = int(input())
    
    # Call the group_students function and print the result
    print(group_students(n))

if __name__ == '__main__':
    main()

