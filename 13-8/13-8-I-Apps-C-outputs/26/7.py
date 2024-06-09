
def count_optimal_paths(n, roads):
    # Initialize a dictionary to store the number of optimal paths for each pair of junctions
    optimal_paths = {}

    # Loop through each pair of junctions
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the pair of junctions is not already in the dictionary, add it and set the number of optimal paths to 0
            if (i, j) not in optimal_paths:
                optimal_paths[(i, j)] = 0

    # Loop through each road
    for road in roads:
        # Get the endpoints of the road
        u, v = road

        # If the optimal path between the endpoints has length 2, increment the number of optimal paths for the pair of junctions
        if optimal_paths[(u, v)] == 2:
            optimal_paths[(u, v)] += 1
            optimal_paths[(v, u)] += 1

    # Return the total number of optimal paths
    return sum(optimal_paths.values())

