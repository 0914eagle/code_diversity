
def find_closest_distance(contour_points):
    # Convert contour points to a list of (x, y) tuples
    points = [(x, y) for x, y in contour_points]

    # Find the point on the contour that is closest to the target point (0, 0)
    closest_point = min(points, key=lambda p: abs(p[0]) + abs(p[1]))

    # Find the distance from the target point to the closest point on the contour
    distance = abs(closest_point[0]) + abs(closest_point[1])

    return distance

