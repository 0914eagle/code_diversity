
def get_min_distance(n, p, distances):
    # Sort the distances in ascending order
    distances.sort()
    # Initialize the minimum distance to the car in front
    min_distance = 0
    # Loop through each distance and calculate the minimum distance needed
    for i in range(n):
        min_distance += p * (i + 1)
        min_distance = max(min_distance, distances[i])
    return min_distance

