
def get_max_groups(n):
    # Initialize a list to store the counts of groups of three or more students
    group_counts = []
    
    # Iterate from 3 to n
    for i in range(3, n + 1):
        # Calculate the number of groups of three or more students that can be formed with i students
        num_groups = n // i
        if n % i != 0:
            num_groups += 1
        
        # Add the count of groups to the list
        group_counts.append(num_groups)
    
    # Return the maximum number of groups that can be formed
    return max(group_counts)

def main():
    # Read the number of students from stdin
    n = int(input())
    
    # Call the get_max_groups function and print the result
    print(get_max_groups(n))

if __name__ == '__main__':
    main()

