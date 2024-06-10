
def get_shuffling_operations(n, s, t, shuffling_operations):
    # Initialize a list to store the current position of the marble
    marble_position = [s]
    # Initialize a set to store the possible positions of the marble
    possible_positions = set([s])
    # Initialize a counter to keep track of the number of shuffling operations
    num_shuffling_operations = 0
    
    while t not in possible_positions:
        # Get the current position of the marble
        current_position = marble_position[-1]
        # Get the next position of the marble based on the shuffling operation
        next_position = shuffling_operations[current_position - 1]
        # Add the next position to the list of possible positions
        possible_positions.add(next_position)
        # Add the next position to the list of marble positions
        marble_position.append(next_position)
        # Increment the number of shuffling operations
        num_shuffling_operations += 1
    
    # If the marble has reached the final position, return the number of shuffling operations
    if t in possible_positions:
        return num_shuffling_operations
    # Otherwise, return -1 to indicate that the marble could not have moved to the final position
    else:
        return -1

def main():
    # Read the input data
    n, s, t = map(int, input().split())
    shuffling_operations = list(map(int, input().split()))
    # Call the get_shuffling_operations function to get the minimum number of shuffling operations
    result = get_shuffling_operations(n, s, t, shuffling_operations)
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

