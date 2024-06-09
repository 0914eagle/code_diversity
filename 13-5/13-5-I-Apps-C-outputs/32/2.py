
def get_longest_path(N, M, roads):
    # Initialize a dictionary to store the lengths of simple paths
    path_lengths = {}

    # Iterate over each road
    for road in roads:
        # Get the length of the simple path starting from the first city and ending at the second city
        path_length = get_simple_path_length(N, road[0], road[1], path_lengths)

        # If the path length is greater than the current longest path length, update the longest path length
        if path_length > longest_path_length:
            longest_path_length = path_length

    # Return the longest path length
    return longest_path_length

def get_simple_path_length(N, city1, city2, path_lengths):
    # If the path has already been calculated, return the stored length
    if (city1, city2) in path_lengths:
        return path_lengths[(city1, city2)]

    # If the path has not been calculated, calculate the length
    path_length = 0
    if city1 != city2:
        # Get the length of the simple path starting from the first city and ending at the second city
        path_length = get_simple_path_length(N, city1, city2, path_lengths)

    # Store the length of the simple path in the dictionary
    path_lengths[(city1, city2)] = path_length

    # Return the length of the simple path
    return path_length

