
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()

    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the trench
        x1, y1, x2, y2 = trench

        # Get the midpoint of the trench
        midpoint_x = (x1 + x2) // 2
        midpoint_y = (y1 + y2) // 2

        # Add the midpoint to the set of guard positions
        guard_positions.add((midpoint_x, midpoint_y))

    # Return the number of ways the guards can be placed
    return len(guard_positions)

