
def find_closest_distance(contour_points):
    # Calculate the distance from the contour points to the target point (0, 0)
    distances = [(x**2 + y**2)**0.5 for x, y in contour_points]

    # Find the minimum distance
    min_distance = min(distances)

    # Return the minimum distance
    return min_distance

