
def get_min_distance(x, y, x1, y1, x2, y2):
    # Calculate the distance from the fence post to each corner of the house
    dist_to_corner1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    dist_to_corner2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    dist_to_corner3 = ((x - x1) ** 2 + (y - y2) ** 2) ** 0.5
    dist_to_corner4 = ((x - x2) ** 2 + (y - y1) ** 2) ** 0.5

    # Return the minimum distance
    return min(dist_to_corner1, dist_to_corner2, dist_to_corner3, dist_to_corner4)

