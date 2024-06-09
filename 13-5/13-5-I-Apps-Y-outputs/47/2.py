
def solve(n, p, distances):
    # Sort the distances in non-decreasing order
    distances.sort()
    # Initialize the minimum distance to the car in front
    min_distance = 0
    # Loop through each car and calculate the minimum distance
    for i in range(n):
        # Calculate the distance to the current car
        distance = distances[i]
        # Calculate the minimum distance to the car in front
        min_distance = max(min_distance, distance - p * (i + 1))
    return min_distance

