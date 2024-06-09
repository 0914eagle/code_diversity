
def solve(n, p, distances):
    # Sort the distances in ascending order
    distances.sort()

    # Initialize the minimum distance to the car in front
    min_distance = 0

    # Loop through each distance and calculate the minimum distance required
    for i in range(n):
        min_distance += p * (i + 1)
        if distances[i] < min_distance:
            return distances[i]

    # If all distances are greater than the minimum distance, return the minimum distance
    return min_distance

