
def is_possible_to_create_loop(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the loop with the first point
    loop = [sorted_points[0]]

    # Iterate through the remaining points
    for i in range(1, len(sorted_points)):
        # Get the current point and the previous point in the loop
        current_point = sorted_points[i]
        previous_point = loop[-1]

        # Check if the current point is parallel to the x-axis and is not already in the loop
        if current_point[1] == previous_point[1] and current_point not in loop:
            # Add the current point to the loop
            loop.append(current_point)
        else:
            # Check if the current point is perpendicular to the previous point in the loop
            if previous_point[0] != current_point[0] and previous_point[1] != current_point[1]:
                # Add the current point to the loop
                loop.append(current_point)
            else:
                # The loop is not possible
                return False

    # Check if the loop goes through all the points
    if len(loop) != len(points):
        return False

    # Check if the loop is valid (i.e., it does not self-intersect)
    for i in range(len(loop) - 1):
        for j in range(i + 1, len(loop)):
            if loop[i] == loop[j]:
                return False

    # The loop is valid
    return True

