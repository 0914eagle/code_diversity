
def get_minimum_inspectors(n, d):
    # Initialize a list to store the inspectors
    inspectors = []

    # Loop through each tree
    for i in range(1, n + 1):
        # Check if the tree is not already inspected
        if i not in inspectors:
            # Add the tree to the inspectors list
            inspectors.append(i)
            # Check if the inspectors list is long enough
            if len(inspectors) == d:
                # Return the minimum number of inspectors
                return len(inspectors)

    # If we reach this point, it means that we need to deploy more inspectors
    return n

def main():
    # Read the input from stdin
    n, d = map(int, input().split())

    # Call the get_minimum_inspectors function
    result = get_minimum_inspectors(n, d)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

