
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    paths = {}

    # Loop through each fragment
    for i in range(n):
        # Initialize the shortest path length from this fragment to the assembly node as infinity
        paths[i] = float('inf')

        # Loop through each node in the system
        for j in range(1, 5001):
            # If the fragment is located at this node, set the shortest path length to 0
            if j == k[i]:
                paths[i] = 0
                break

            # If the fragment is not located at this node, check if the node is a factorial of another node
            if j % k[i] == 0:
                # If the fragment is located at a factorial of this node, set the shortest path length to 1
                paths[i] = 1
                break

    # Return the sum of the shortest path lengths for all fragments
    return sum(paths.values())

