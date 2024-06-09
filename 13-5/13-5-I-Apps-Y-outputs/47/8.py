
def get_min_distance(n, p, distances):
    # Sort the distances in ascending order
    sorted_distances = sorted(distances)

    # Initialize the minimum distance to the car in front
    min_distance = 0

    # Iterate through the distances and calculate the minimum distance
    for i in range(n):
        min_distance += sorted_distances[i] * (p + 1)

    return min_distance

