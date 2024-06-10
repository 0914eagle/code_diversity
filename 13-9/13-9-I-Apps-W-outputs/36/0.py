
def get_shuffling_operations(n, s, t, shuffling_operation_parameters):
    # Initialize a list to store the positions of the glasses after each shuffling operation
    glass_positions = list(range(1, n+1))
    
    # Initialize a set to store the positions of the glasses that have been shuffled
    shuffled_positions = set()
    
    # Initialize a variable to store the number of shuffling operations performed
    num_shuffling_operations = 0
    
    # Loop through the shuffling operation parameters
    for p in shuffling_operation_parameters:
        # Check if the marble is in the position where the glass is being shuffled
        if glass_positions[s-1] == p:
            # Add the position of the glass being shuffled to the set of shuffled positions
            shuffled_positions.add(p)
            # Update the position of the marble
            s = p
        # Check if the marble is in the position where the glass is being shuffled back to its original position
        elif glass_positions[p-1] == s:
            # Remove the position of the glass being shuffled from the set of shuffled positions
            shuffled_positions.remove(p)
            # Update the position of the marble
            s = p
        # Check if the marble is in the position where the glass is being shuffled and the glass has been shuffled before
        elif glass_positions[s-1] == p and p in shuffled_positions:
            # Update the position of the marble
            s = p
        # Check if the marble is in the position where the glass is being shuffled and the glass has not been shuffled before
        elif glass_positions[s-1] == p and p not in shuffled_positions:
            # Add the position of the glass being shuffled to the set of shuffled positions
            shuffled_positions.add(p)
            # Update the position of the marble
            s = p
            # Increment the number of shuffling operations performed
            num_shuffling_operations += 1
    
    # Check if the marble has moved to the final position
    if glass_positions[s-1] == t:
        # Return the number of shuffling operations performed
        return num_shuffling_operations
    else:
        # Return -1 to indicate that the marble could not move to the final position
        return -1

def main():
    # Read the input
    n, s, t = map(int, input().split())
    shuffling_operation_parameters = list(map(int, input().split()))
    
    # Call the get_shuffling_operations function
    result = get_shuffling_operations(n, s, t, shuffling_operation_parameters)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

