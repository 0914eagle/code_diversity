
def solve(n, distances):
    # Sort the distances in non-decreasing order
    distances.sort()

    # Initialize the maximum number of locations to 0
    max_locations = 0

    # Iterate over the distances and find the maximum number of locations
    for i in range(n):
        # If the distance is greater than or equal to the current location, increment the location count
        if distances[i] >= i:
            max_locations += 1

    # Return the maximum number of locations
    return max_locations

