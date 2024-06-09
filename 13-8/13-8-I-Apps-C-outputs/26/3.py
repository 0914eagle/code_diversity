
def solve(N, roads):
    # Initialize a dictionary to store the number of optimal paths of length 2 for each junction
    optimal_paths = {junction: 0 for junction in range(1, N + 1)}

    # Iterate over each road
    for u, v in roads:
        # If the path between the two endpoints has length 2, increment the number of optimal paths for both endpoints
        if u != v:
            optimal_paths[u] += 1
            optimal_paths[v] += 1

    # Return the sum of the number of optimal paths for all junctions
    return sum(optimal_paths.values())

