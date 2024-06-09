
def solve(n, distances):
    # Sort the distances in non-decreasing order
    distances.sort()

    # Initialize the maximum number of locations to 0
    max_locations = 0

    # Iterate over the distances and find the maximum number of locations
    for i in range(n):
        # If the distance is less than or equal to the current location, it means the shark is still in the same location
        if distances[i] <= i:
            continue
        # Otherwise, the shark has moved to a new location, so increment the number of locations
        max_locations += 1

    return max_locations

