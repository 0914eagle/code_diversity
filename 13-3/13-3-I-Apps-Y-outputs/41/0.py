
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

    # Iterate over the edges and check if they are bridges
    for edge in edges:
        # If the edge is a bridge, increment the number of bridges
        if is_bridge(graph, edge):
            bridges += 1

    return bridges

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

def is_connected(graph, node):
    # Initialize a set to store the visited nodes
    visited = set()

    # Initialize a queue to store the nodes to be visited
    queue = [node]

    # Loop until the queue is empty
    while queue:
        # Get the first node from the queue
        node = queue.pop(0)

        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            queue += graph[node]

    # If all nodes have been visited, the graph is connected
    return len(visited) == len(graph)

n, m = map(int, input().split())
edges = []
for i in range(m):
    edges.append(list(map(int, input().split())))

print(get_bridges(n, m, edges))

