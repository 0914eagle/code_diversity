
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the two ends of the trench
        x1, y1, x2, y2 = trench
        # Check if the guard positions are on the same line segment
        if x1 == x2 or y1 == y2:
            # If the guard positions are on the same line segment, add them to the set
            guard_positions.add((x1, y1))
            guard_positions.add((x2, y2))
    # Return the number of ways the guards can be placed
    return len(guard_positions)

