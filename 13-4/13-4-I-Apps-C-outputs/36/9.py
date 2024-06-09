
def get_number_of_ways(trenches):
    # Initialize a set to store the coordinates of the guards
    guard_coordinates = set()

    # Iterate over the trenches
    for trench in trenches:
        # Get the coordinates of the ends of the trench
        x1, y1, x2, y2 = trench

        # If the trench is horizontal or vertical, add the coordinates of the ends to the set
        if x1 == x2 or y1 == y2:
            guard_coordinates.add((x1, y1))
            guard_coordinates.add((x2, y2))

    # Return the number of ways the guards can be placed
    return len(guard_coordinates)

