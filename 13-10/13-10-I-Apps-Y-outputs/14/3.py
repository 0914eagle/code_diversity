
def get_maximum_groups(n):
    # Initialize a list to store the groups
    groups = []
    
    # Iterate from 3 to n
    for i in range(3, n + 1):
        # Check if the current number is divisible by 3
        if n % i == 0:
            # Add the current number to the list of groups
            groups.append(i)
    
    # Return the length of the list of groups
    return len(groups)

def main():
    # Read a single integer from stdin and save it in the variable n
    n = int(input())
    
    # Call the get_maximum_groups function and save its return value in the variable result
    result = get_maximum_groups(n)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

