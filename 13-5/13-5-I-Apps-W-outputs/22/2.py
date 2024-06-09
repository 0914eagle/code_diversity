
def solve(n, permutation, sequence):
    # Initialize a list to store the positions of the skewers
    positions = [i for i in range(1, n + 1)]
    # Initialize a set to store the visited positions
    visited = set()
    # Initialize a variable to store the number of changes needed
    changes = 0

    for i in range(n):
        # Get the current position of the skewer
        current = permutation[i]
        # Get the direction of the skewer
        direction = sequence[i]
        # If the skewer is not visited, add it to the visited set
        if current not in visited:
            visited.add(current)
        # If the skewer is visited and the direction is 1, reverse the skewer
        elif direction == 1:
            # Get the index of the current position in the positions list
            index = positions.index(current)
            # Reverse the positions list from the current position to the end
            positions[index:] = reversed(positions[index:])
            # Increment the number of changes needed
            changes += 1

    # Return the number of changes needed
    return changes

