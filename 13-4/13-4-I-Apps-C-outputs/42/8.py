
def get_min_path_length(n, k):
    # Initialize a dictionary to store the shortest distance from each fragment to the assembly node
    distances = {}
    
    # Loop through each fragment
    for i in range(n):
        # Initialize the shortest distance from this fragment to the assembly node as infinity
        distances[i] = float('inf')
    
    # Loop through each fragment
    for i in range(n):
        # Loop through each node in the graph
        for j in range(1, k[i]! + 1):
            # If the current node is the node where the current fragment is located
            if j == k[i]!:
                # The shortest distance from this fragment to the assembly node is 0
                distances[i] = 0
            # If the current node is not the node where the current fragment is located
            else:
                # The shortest distance from this fragment to the assembly node is the minimum of the current distance and the distance from the current fragment to the node where the current fragment is located plus the distance from the node where the current fragment is located to the assembly node
                distances[i] = min(distances[i], distances.get(j, float('inf')) + 1)
    
    # Return the sum of the shortest distances from each fragment to the assembly node
    return sum(distances.values())

