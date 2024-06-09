
def topologically_sort(graph):
    # Initialize the list of source nodes
    sources = [node for node in graph if not node.in_degree]
    # Initialize the sorted list
    sorted_list = []
    # Loop until there are no more sources
    while sources:
        # Get the source node with the minimum index
        source = min(sources, key=lambda x: x.index)
        # Remove the source node and its outgoing edges
        sources.remove(source)
        for edge in list(source.out_edges):
            edge.target.in_degree -= 1
            if edge.target.in_degree == 0:
                sources.append(edge.target)
        # Add the source node to the sorted list
        sorted_list.append(source)
    # Return the sorted list
    return sorted_list

def kahn_algorithm(graph):
    # Initialize the list of source nodes
    sources = [node for node in graph if not node.in_degree]
    # Initialize the sorted list
    sorted_list = []
    # Loop until there are no more sources
    while sources:
        # Get the source node with the minimum index
        source = min(sources, key=lambda x: x.index)
        # Remove the source node and its outgoing edges
        sources.remove(source)
        for edge in list(source.out_edges):
            edge.target.in_degree -= 1
            if edge.target.in_degree == 0:
                sources.append(edge.target)
        # Add the source node to the sorted list
        sorted_list.append(source)
    # Return the sorted list
    return sorted_list

def main():
    # Read the input graph
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
    # Topologically sort the graph
    sorted_list = kahn_algorithm(graph)
    # Print the largest possible size of S at the beginning of Step 1
    print(len(sorted_list))

if __name__ == "__main__":
    main()

