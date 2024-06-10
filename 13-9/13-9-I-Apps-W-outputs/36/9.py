
def get_shuffling_operations(n, s, t, p):
    # Initialize a list to store the positions of the glasses
    glasses = list(range(1, n+1))
    # Initialize a variable to store the number of shuffling operations
    operations = 0
    # Loop through the shuffling operation parameters
    for i in range(n):
        # Check if the marble is in the correct position
        if glasses[s-1] == t:
            # If the marble is in the correct position, return the number of shuffling operations
            return operations
        # If the marble is not in the correct position, perform the shuffling operation
        glasses[s-1], glasses[p[i]-1] = glasses[p[i]-1], glasses[s-1]
        # Increment the number of shuffling operations
        operations += 1
    # If the marble could not be moved to the correct position, return -1
    return -1

def main():
    # Read the input data
    n, s, t = map(int, input().split())
    p = list(map(int, input().split()))
    # Call the get_shuffling_operations function and print the result
    print(get_shuffling_operations(n, s, t, p))

if __name__ == '__main__':
    main()

