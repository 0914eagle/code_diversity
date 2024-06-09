
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a variable to store the number of bridges
    bridges = 0

    # Iterate through the edges and check if they are bridges
    for edge in edges:
        # If the edge is a bridge, increment the number of bridges
        if is_bridge(graph, edge):
            bridges += 1

    return bridges

# Check if an edge is a bridge
def is_bridge(graph, edge):
    # Remove the edge from the graph
    graph[edge[0]].remove(edge[1])
    graph[edge[1]].remove(edge[0])

    # Check if the graph is still connected
    connected = is_connected(graph, edge[0])

    # Add the edge back to the graph
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])

    return not connected

# Check if the graph is connected from a given vertex
def is_connected(graph, vertex):
    # Initialize a queue to store the vertices to visit
    queue = [vertex]

    # Initialize a set to store the visited vertices
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]

    # If all vertices have been visited, the graph is connected
    return len(visited) == len(graph)

