
def solve(n, d):
    # Initialize a list to store the inspectors
    inspectors = []
    # Iterate through the trees
    for i in range(1, n + 1):
        # Check if the tree is a golden apple tree
        if i % 2 == 0:
            # Add the inspector to the list
            inspectors.append(i)
    # Return the minimum number of inspectors needed
    return len(inspectors)

def main():
    # Read the input from stdin
    n, d = map(int, input().split())
    # Call the solve function and print the result
    print(solve(n, d))

if __name__ == '__main__':
    main()

