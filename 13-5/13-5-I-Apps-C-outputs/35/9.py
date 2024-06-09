
def count_intersections(lines):
    # Initialize a set to store the unique points
    points = set()

    # Iterate over the lines
    for line in lines:
        # Get the endpoints of the line
        x1, y1, x2, y2 = line

        # Check if the line is horizontal, vertical, or diagonal
        if x1 == x2:
            # Line is horizontal, add the y-coordinate of the endpoints to the set
            points.add(y1)
            points.add(y2)
        elif y1 == y2:
            # Line is vertical, add the x-coordinate of the endpoints to the set
            points.add(x1)
            points.add(x2)
        else:
            # Line is diagonal, add the endpoints to the set
            points.add((x1, y1))
            points.add((x2, y2))

    # Return the number of unique points
    return len(points)

