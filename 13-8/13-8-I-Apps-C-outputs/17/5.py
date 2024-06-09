
def get_number_of_ways(trenches):
    # Initialize a set to store the guards' positions
    guard_positions = set()
    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the trench ends
        x1, y1, x2, y2 = trench
        # Check if the trench is vertical or horizontal
        if x1 == x2:
            # Trench is vertical, add the guard positions to the set
            for y in range(min(y1, y2), max(y1, y2) + 1):
                guard_positions.add((x1, y))
        elif y1 == y2:
            # Trench is horizontal, add the guard positions to the set
            for x in range(min(x1, x2), max(x1, x2) + 1):
                guard_positions.add((x, y1))
        else:
            # Trench is diagonal, add the guard positions to the set
            for i in range(abs(x2 - x1) + 1):
                guard_positions.add((x1 + i, y1 + i))
    # Return the number of ways the guards can be placed
    return len(guard_positions)

