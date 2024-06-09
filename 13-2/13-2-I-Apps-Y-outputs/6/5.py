
def get_min_distance(x, y, x1, y1, x2, y2):
    # Calculate the distance from the fence post to each corner of the house
    dist_to_corner_1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
    dist_to_corner_2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    dist_to_corner_3 = ((x - x1) ** 2 + (y - y2) ** 2) ** 0.5
    dist_to_corner_4 = ((x - x2) ** 2 + (y - y1) ** 2) ** 0.5

    # Return the minimum distance
    return min(dist_to_corner_1, dist_to_corner_2, dist_to_corner_3, dist_to_corner_4)

