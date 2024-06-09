
def solve(n, p, distances):
    # Sort the distances in non-decreasing order
    distances.sort()
    # Initialize the minimum distance to the car in front
    min_distance = 0
    # Loop through each distance and calculate the minimum distance required
    for i in range(n):
        min_distance += p * (i + 1)
        if distances[i] < min_distance:
            return min_distance
    return min_distance

