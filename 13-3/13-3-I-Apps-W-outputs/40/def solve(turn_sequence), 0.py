
def solve(turn_sequence):
    # Convert the turn sequence to a list of directions
    directions = list(turn_sequence)

    # Initialize a list to store the possible unlock patterns
    unlock_patterns = []

    # Iterate through the possible directions at each pivot
    for direction in directions:
        # If the direction is a question mark, add all four possible directions to the list
        if direction == '?':
            unlock_patterns.append('L')
            unlock_patterns.append('R')
            unlock_patterns.append('S')
            unlock_patterns.append('A')
        # Otherwise, add the current direction to the list
        else:
            unlock_patterns.append(direction)

    # Return the number of possible unlock patterns
    return len(unlock_patterns)

