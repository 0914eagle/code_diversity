
def count_optimal_paths(n, roads):
    # Initialize a dictionary to store the number of optimal paths for each pair of junctions
    optimal_paths = {}

    # Loop through each road
    for road in roads:
        # Get the two endpoints of the road
        u, v = road

        # If there is no path from u to v, add a path of length 1
        if (u, v) not in optimal_paths:
            optimal_paths[(u, v)] = 1

        # If there is a path from u to v, add a path of length 2
        if (v, u) in optimal_paths:
            optimal_paths[(u, v)] += optimal_paths[(v, u)]

    # Return the total number of optimal paths
    return sum(optimal_paths.values())

