
def solve(N, trenches):
    # Initialize a set to store the guard positions
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the start and end points of the trench
        start, end = trench[0], trench[1]
        # Check if the guard positions are already present in the set
        if start in guard_positions and end in guard_positions:
            # If both points are already present, return 0
            return 0
        # Add the start and end points to the set
        guard_positions.add(start)
        guard_positions.add(end)
    # If all guards are placed, return the number of ways they can be placed
    return len(guard_positions)

