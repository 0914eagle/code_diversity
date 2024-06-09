
def get_min_distance(n, p, distances):
    # Sort the distances in non-decreasing order
    distances.sort()
    # Initialize the minimum distance to the car in front
    min_distance = 1
    # Iterate through the distances
    for i in range(n):
        # Calculate the distance needed to maintain the minimum speed
        distance_needed = (i + 1) * p
        # If the current distance is less than the distance needed, update the minimum distance
        if distances[i] < distance_needed:
            min_distance = distance_needed
    return min_distance

