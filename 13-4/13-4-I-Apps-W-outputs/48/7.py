
def solve(n, a):
    # Initialize variables
    points = set()
    infinite = False

    # Iterate over each figure
    for i in range(n):
        # Get the type of the current figure
        current_type = a[i]

        # If the current figure is a circle
        if current_type == 1:
            # Add the center of the circle to the set of points
            points.add((0, 0))

        # If the current figure is a square
        elif current_type == 2:
            # Add the four corners of the square to the set of points
            points.update([(0, 0), (1, 0), (1, 1), (0, 1)])

        # If the current figure is an isosceles triangle
        elif current_type == 3:
            # Add the three vertices of the triangle to the set of points
            points.update([(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)])

        # If the current figure is inscribed into the previous figure
        if i > 0:
            # Get the type of the previous figure
            previous_type = a[i - 1]

            # If the previous figure is a circle
            if previous_type == 1:
                # Add the center of the circle to the set of points
                points.add((0, 0))

            # If the previous figure is a square
            elif previous_type == 2:
                # Add the four corners of the square to the set of points
                points.update([(0, 0), (1, 0), (1, 1), (0, 1)])

            # If the previous figure is an isosceles triangle
            elif previous_type == 3:
                # Add the three vertices of the triangle to the set of points
                points.update([(0, 0), (1, 0), (0.5, math.sqrt(3) / 2)])

    # If the set of points contains at least one infinite point
    if any(point == (float('inf'), float('inf')) for point in points):
        infinite = True

    # Return the number of distinct points
    return "Infinite" if infinite else len(points)

