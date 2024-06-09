
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the start and end positions of the trench
        start_position = (trench[0], trench[1])
        end_position = (trench[2], trench[3])
        # If the start and end positions are the same, skip this trench
        if start_position == end_position:
            continue
        # If the trench is horizontal or vertical
        if start_position[0] == end_position[0] or start_position[1] == end_position[1]:
            # Add the start and end positions to the set of guard positions
            guard_positions.add(start_position)
            guard_positions.add(end_position)
        # If the trench is diagonal
        else:
            # Get the slope and y-intercept of the line
            slope = (end_position[1] - start_position[1]) / (end_position[0] - start_position[0])
            y_intercept = start_position[1] - slope * start_position[0]
            # Iterate over the positions between the start and end positions, inclusive
            for x in range(min(start_position[0], end_position[0]), max(start_position[0], end_position[0]) + 1):
                y = slope * x + y_intercept
                guard_position = (x, int(y))
                # Add the position to the set of guard positions
                guard_positions.add(guard_position)
    # Return the number of ways the guards can be placed
    return len(guard_positions)

