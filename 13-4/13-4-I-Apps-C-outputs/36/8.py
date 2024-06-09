
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()

    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the trench
        x1, y1, x2, y2 = trench

        # Get the position of the guard at the first end of the trench
        guard_position = (x1, y1)

        # If the guard position is not already in the set, add it
        if guard_position not in guard_positions:
            guard_positions.add(guard_position)

        # Get the position of the guard at the second end of the trench
        guard_position = (x2, y2)

        # If the guard position is not already in the set, add it
        if guard_position not in guard_positions:
            guard_positions.add(guard_position)

    # Return the number of ways the guards can be placed
    return len(guard_positions)

