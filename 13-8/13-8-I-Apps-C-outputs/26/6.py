
def count_optimal_paths(n, roads):
    # Initialize a dictionary to store the number of optimal paths for each pair of junctions
    optimal_paths = {}

    # Loop through each road and increment the number of optimal paths for each pair of junctions
    for u, v in roads:
        if (u, v) not in optimal_paths:
            optimal_paths[(u, v)] = 1
        else:
            optimal_paths[(u, v)] += 1

    # Return the total number of optimal paths
    return sum(optimal_paths.values())

