
def kahn_algorithm(graph):
    # Initialize the list of source nodes and the sorted list
    sources = [node for node in graph if not graph[node]]
    sorted_list = []

    # While there are sources nodes, iterate through them
    while sources:
        # Get the current source node and remove it from the graph
        current_source = sources.pop(0)
        graph.pop(current_source)

        # Add the current source node to the sorted list
        sorted_list.append(current_source)

        # Find all nodes that have an edge to the current source node and remove the edge
        for node in graph:
            if current_source in graph[node]:
                graph[node].remove(current_source)

                # If the node now has no incoming edges, add it to the sources list
                if not graph[node]:
                    sources.append(node)

    # If the graph is empty, return the sorted list, otherwise return -1
    return sorted_list if not graph else -1

def largest_s(graph):
    # Initialize the largest size of S to 0
    largest_size = 0

    # Iterate through all possible choices of alpha
    for alpha in range(len(graph)):
        # Clone the graph and apply Kahn's algorithm
        graph_copy = graph.copy()
        sorted_list = kahn_algorithm(graph_copy)

        # If the graph is not empty, continue to the next iteration
        if sorted_list == -1:
            continue

        # If the size of S is larger than the current largest size, update the largest size
        if len(sorted_list) > largest_size:
            largest_size = len(sorted_list)

    # Return the largest size of S
    return largest_size

# Test the function with the sample input
graph = {0: [1], 1: [2], 2: [3], 3: []}
print(largest_s(graph))

# Test the function with a larger input
graph = {0: [1, 2], 1: [3], 2: [4], 3: [5], 4: [6], 5: [6], 6: []}
print(largest_s(graph))

