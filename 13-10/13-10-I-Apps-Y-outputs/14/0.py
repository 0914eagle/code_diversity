
def divide_students(n):
    # Initialize a list to store the groups
    groups = []
    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Check if the current number is a divisor of n
        if n % i == 0:
            # If it is, add it to the list of groups
            groups.append(i)
    # Return the length of the list of groups
    return len(groups)

def main():
    # Read a single integer from stdin and save it in the variable n
    n = int(input())
    # Call the divide_students function and save its return value in the variable result
    result = divide_students(n)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

