
def count_paths(graph):
    # Initialize a list to store the number of paths for each vertex
    num_paths = [0] * len(graph)
    # Initialize the number of paths for vertex 1 as 1
    num_paths[0] = 1
    # Iterate through the graph
    for i in range(len(graph)):
        # Iterate through the neighbors of the current vertex
        for neighbor in graph[i]:
            # If the neighbor has not been visited yet, increment the number of paths for the neighbor
            if num_paths[neighbor] == 0:
                num_paths[neighbor] += num_paths[i]
    # Return the number of paths for vertex N
    return num_paths[-1]

