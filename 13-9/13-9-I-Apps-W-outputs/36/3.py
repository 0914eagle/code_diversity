
def get_shuffling_operations(n, s, t, shuffling_operations):
    # Initialize a list to store the position of the marble after each shuffling operation
    positions = [s]
    # Initialize a variable to store the minimum number of shuffling operations needed
    min_operations = 0
    # Loop through each shuffling operation
    for operation in shuffling_operations:
        # Check if the marble has reached the final position
        if positions[-1] == t:
            break
        # Update the position of the marble after the shuffling operation
        positions.append(operation)
        # Increment the minimum number of shuffling operations needed
        min_operations += 1
    # Check if the marble has reached the final position
    if positions[-1] != t:
        return -1
    # Return the minimum number of shuffling operations needed
    return min_operations

def main():
    # Read the input data
    n, s, t = map(int, input().split())
    shuffling_operations = list(map(int, input().split()))
    # Call the get_shuffling_operations function
    result = get_shuffling_operations(n, s, t, shuffling_operations)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

