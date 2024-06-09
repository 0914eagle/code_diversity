
def solve(N, trenches):
    # Initialize a set to store the positions of the guards
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the start and end positions of the trench
        start, end = trench[0], trench[1]
        # Check if the guard positions are between the start and end positions
        for guard in guard_positions:
            if start[0] <= guard[0] <= end[0] and start[1] <= guard[1] <= end[1]:
                # If the guard position is between the start and end positions, remove it from the set
                guard_positions.remove(guard)
    # Return the number of remaining guard positions
    return len(guard_positions)

