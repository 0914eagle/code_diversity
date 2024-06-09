
def get_closest_distance(contour_points):
    # Convert contour points to a list of (x, y) tuples
    points = [(x, y) for x, y in contour_points]

    # Find the point on the contour that is closest to the target point (0, 0)
    closest_point = min(points, key=lambda p: abs(p[0]) + abs(p[1]))

    # Calculate the distance from the target point to the closest point on the contour
    distance = ((closest_point[0] - 0) ** 2 + (closest_point[1] - 0) ** 2) ** 0.5

    return distance

