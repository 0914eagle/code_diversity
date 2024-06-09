
def get_min_path_length(n, k_list):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    path_lengths = {}

    # Loop through each fragment
    for i in range(n):
        # Initialize the shortest path length from this fragment to the assembly node as infinity
        path_lengths[i] = float('inf')

        # Loop through each node in the graph
        for node in range(1, n + 1):
            # If the fragment is located at this node, the shortest path length is 0
            if node == k_list[i]:
                path_lengths[i] = 0
                break

            # If the fragment is not located at this node, check if the node is connected to the fragment's current node
            elif node % k_list[i] == 0:
                # If the node is connected, update the shortest path length if necessary
                path_lengths[i] = min(path_lengths[i], path_lengths[node // k_list[i]] + 1)

    # Return the sum of the shortest path lengths from all fragments to the assembly node
    return sum(path_lengths.values())

