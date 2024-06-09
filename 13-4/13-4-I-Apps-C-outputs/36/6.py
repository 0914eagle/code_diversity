
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()

    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the two ends of the trench
        x1, y1, x2, y2 = trench

        # If the trench is horizontal or vertical
        if x1 == x2 or y1 == y2:
            # Add the midpoint of the trench to the set of guard positions
            guard_positions.add(((x1 + x2) // 2, (y1 + y2) // 2))

    # Return the number of ways the guards can be placed
    return len(guard_positions)

