
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest path length from each fragment to the assembly node
    shortest_path_lengths = {}

    # Loop through each fragment
    for i in range(n):
        # Initialize the shortest path length for this fragment to infinity
        shortest_path_lengths[i] = float('inf')

        # Loop through each node in the graph
        for j in range(1, k[i]! + 1):
            # If the current node is the assembly node, set the shortest path length to 0
            if j == k[i]!:
                shortest_path_lengths[i] = 0
                break

            # If the current node is not the assembly node, find the shortest path length from the current node to the assembly node
            shortest_path_lengths[i] = min(shortest_path_lengths[i], get_shortest_path_length(j, k[i]!))

    # Return the sum of the shortest path lengths for all fragments
    return sum(shortest_path_lengths.values())

def get_shortest_path_length(start, end):
    # Initialize a dictionary to store the shortest path length from the start node to each node in the graph
    shortest_path_lengths = {start: 0}

    # Loop through each node in the graph
    for i in range(1, end + 1):
        # If the current node is the end node, return the shortest path length
        if i == end:
            return shortest_path_lengths[i]

        # If the current node is not the end node, find the shortest path length from the current node to the end node
        shortest_path_lengths[i] = min(shortest_path_lengths[i], get_shortest_path_length(i, end))

    # Return the shortest path length from the start node to the end node
    return shortest_path_lengths[end]

