
def is_loop_possible(points):
    
    # Check if the number of points is even
    if len(points) % 2 == 1:
        return False

    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Iterate through the points and check if they form a valid loop
    for i in range(len(sorted_points)):
        # Get the current point and the next point
        current_point = sorted_points[i]
        next_point = sorted_points[(i + 1) % len(sorted_points)]

        # Check if the current point is a consecutive point of the next point
        if current_point[1] != next_point[1]:
            return False

    return True

