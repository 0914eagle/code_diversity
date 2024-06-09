
def solve(n, permutation, sequence):
    # Initialize variables
    total_changes = 0
    visited_positions = set()
    visited_reversed_positions = set()

    # Iterate through the permutation and sequence
    for i in range(n):
        # Get the current position and reversed position
        position = permutation[i]
        reversed_position = n - position + 1

        # If the current position has not been visited, add it to the visited set
        if position not in visited_positions:
            visited_positions.add(position)

        # If the reversed position has not been visited, add it to the visited set
        if reversed_position not in visited_reversed_positions:
            visited_reversed_positions.add(reversed_position)

        # If the current position and reversed position have been visited, increment the total changes
        if position in visited_positions and reversed_position in visited_reversed_positions:
            total_changes += 1

    # Return the total changes
    return total_changes

