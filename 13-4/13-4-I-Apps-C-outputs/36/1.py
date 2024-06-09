
def get_number_of_ways(trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the start and end points of the trench
        start_point, end_point = trench[0], trench[1]
        # Check if the start point is already in the set of guard positions
        if start_point not in guard_positions:
            # If not, add it to the set
            guard_positions.add(start_point)
        # Check if the end point is already in the set of guard positions
        if end_point not in guard_positions:
            # If not, add it to the set
            guard_positions.add(end_point)
    # Return the number of ways the guards can be placed
    return len(guard_positions)

