
def get_symmetry(spots):
    # Find the center of mass of the spots
    center_x = sum(x for x, y in spots) / len(spots)
    center_y = sum(y for x, y in spots) / len(spots)

    # Calculate the distance of each spot from the center
    distances = [(x - center_x) ** 2 + (y - center_y) ** 2 for x, y in spots]

    # Find the minimum distance
    min_distance = min(distances)

    # Count the number of spots with the minimum distance
    num_spots = distances.count(min_distance)

    # Return the number of spots needed to be added
    return num_spots

