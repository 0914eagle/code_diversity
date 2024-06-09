
def get_bridges(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize a list to store the bridges
    bridges = []

    # Iterate over the edges and check if they are bridges
    for edge in edges:
        # If the edge is a bridge, add it to the list of bridges
        if is_bridge(graph, edge):
            bridges.append(edge)

    # Return the number of bridges
    return len(bridges)

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

    # Return True if the edge is a bridge, False otherwise
    return not connected

# Check if the graph is still connected after removing an edge
def is_connected(graph, start):
    # Initialize a set to store the visited vertices
    visited = set()

    # Initialize a queue to store the vertices to be visited
    queue = [start]

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]

    # Return True if all vertices have been visited, False otherwise
    return len(visited) == len(graph)

# Main function
def main():
    # Read the input
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))

    # Find the number of bridges
    bridges = get_bridges(n, m, edges)

    # Print the number of bridges
    print(bridges)

if __name__ == "__main__":
    main()

