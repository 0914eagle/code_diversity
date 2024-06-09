
def get_guard_placements(trenches):
    # Initialize a set to store the guard placements
    guard_placements = set()

    # Loop through each trench
    for trench in trenches:
        # Get the coordinates of the trench ends
        x1, y1, x2, y2 = trench

        # Check if the trench is horizontal or vertical
        if x1 == x2 or y1 == y2:
            # If the trench is horizontal, check if it intersects with the other trenches
            if x1 == x2:
                # If the trench is horizontal and intersects with the other trenches, add it to the guard placements
                guard_placements.add((x1, y1))
                guard_placements.add((x2, y2))
            else:
                # If the trench is vertical and intersects with the other trenches, add it to the guard placements
                guard_placements.add((x1, y1))
                guard_placements.add((x1, y2))

    # Return the number of guard placements
    return len(guard_placements)

