
def kahn_algorithm(graph):
    
    # Initialize the list of source nodes (nodes with no incoming edges)
    source_nodes = [node for node in graph if not graph[node]]
    sorted_nodes = []
    while source_nodes:
        # Select an arbitrary source node and remove it from the graph
        node = source_nodes.pop()
        graph.pop(node)
        # Remove the outgoing edges of the selected node and add the new source nodes to the list of source nodes
        for neighbor in graph[node]:
            graph[neighbor].remove(node)
            if not graph[neighbor]:
                source_nodes.append(neighbor)
        # Add the selected node to the sorted list
        sorted_nodes.append(node)
    return sorted_nodes

def largest_source_nodes(graph):
    
    # Initialize the list of source nodes (nodes with no incoming edges)
    source_nodes = [node for node in graph if not graph[node]]
    largest_size = 0
    while source_nodes:
        # Select an arbitrary source node and remove it from the graph
        node = source_nodes.pop()
        graph.pop(node)
        # Remove the outgoing edges of the selected node and add the new source nodes to the list of source nodes
        for neighbor in graph[node]:
            graph[neighbor].remove(node)
            if not graph[neighbor]:
                source_nodes.append(neighbor)
        # Update the largest size of S
        largest_size = max(largest_size, len(source_nodes))
    return largest_size

def main():
    # Read the input data
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        x, y = map(int, input().split())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
    # Find the largest possible size of S at the beginning of any iteration of Step 1 in the execution of Kahn's Algorithm
    largest_size = largest_source_nodes(graph)
    print(largest_size)

if __name__ == "__main__":
    main()

