
def get_max_apples(n, positions, apples):
    # Sort the positions and apples arrays based on the position
    sorted_positions = sorted(positions)
    sorted_apples = [apples[i] for i in range(n) if positions[i] in sorted_positions]

    # Initialize the maximum number of apples and the current position
    max_apples = 0
    current_position = 0

    # Iterate through the sorted positions and apples arrays
    for i in range(n):
        # If the current position is not the same as the current position, move to the next position
        if sorted_positions[i] != current_position:
            current_position = sorted_positions[i]

        # Add the number of apples at the current position to the maximum number of apples
        max_apples += sorted_apples[i]

    return max_apples

