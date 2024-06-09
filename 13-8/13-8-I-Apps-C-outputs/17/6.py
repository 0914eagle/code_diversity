
def solve(N, trenches):
    # Initialize a set to store the guards' positions
    guards = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the trench
        x1, y1, x2, y2 = trench
        # Check if the trench is horizontal or vertical
        if x1 == x2 or y1 == y2:
            # If the trench is horizontal, add its middle point to the set of guards' positions
            if x1 == x2:
                guards.add((x1, (y1 + y2) // 2))
            # If the trench is vertical, add its middle point to the set of guards' positions
            else:
                guards.add(((x1 + x2) // 2, y1))
    # Return the number of ways the guards can be placed
    return len(guards)

