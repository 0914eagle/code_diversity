
def get_min_inspectors(N, D):
    # Initialize the number of inspectors to 0
    num_inspectors = 0
    
    # Loop through each tree
    for i in range(1, N + 1):
        # Check if the tree is within the range of an inspector's inspection
        if i - D <= 0 or i + D >= N:
            # Increment the number of inspectors
            num_inspectors += 1
    
    # Return the minimum number of inspectors
    return num_inspectors

def main():
    # Read the input from stdin
    N, D = map(int, input().split())
    
    # Call the get_min_inspectors function and print the result
    print(get_min_inspectors(N, D))

if __name__ == '__main__':
    main()

