
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest distance from each node to the assembly node
    dist = {1: 0}

    # Loop through each node
    for i in range(2, n + 1):
        # If the node is not in the dictionary, add it with a distance of infinity
        if i not in dist:
            dist[i] = float("inf")

        # Loop through each fragment
        for j in range(len(k)):
            # If the fragment is located at the current node
            if k[j] == i:
                # Update the shortest distance from the current node to the assembly node
                dist[i] = min(dist[i], dist[k[j]] + 1)

    # Return the minimum path length
    return sum(dist.values())

