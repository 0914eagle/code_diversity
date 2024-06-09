
def get_min_distance(n, p, distances):
    # Sort the distances in ascending order
    distances.sort()
    # Initialize the minimum distance to the car in front
    min_distance = 1
    # Loop through the distances and calculate the minimum distance required
    for i in range(n):
        min_distance += p * (i + 1)
        if min_distance > distances[i]:
            break
    return min_distance

