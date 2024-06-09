
def find_minimum_length_path(n, m, roads):
    # Initialize a dictionary to store the length of the path from each station to the finish line
    length_from_finish = {n: 0}

    # Loop through each road
    for u, v in roads:
        # If the length from the finish line to the starting station is not already known, calculate it
        if u not in length_from_finish:
            length_from_finish[u] = length_from_finish[v] + 1
        # If the length from the finish line to the ending station is not already known, calculate it
        if v not in length_from_finish:
            length_from_finish[v] = length_from_finish[u] + 1

    # Return the minimum length path from the starting station to the finish line
    return min(length_from_finish.values())

