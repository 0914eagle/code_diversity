
def get_network_topology(n, edges):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])

    # Check if the graph is connected
    if not is_connected(graph):
        return "unknown topology"

    # Check if the graph is a bus
    if is_bus(graph):
        return "bus topology"

    # Check if the graph is a ring
    if is_ring(graph):
        return "ring topology"

    # Check if the graph is a star
    if is_star(graph):
        return "star topology"

    # If none of the above conditions are met, the topology is unknown
    return "unknown topology"

# Check if the graph is connected by traversing it
def is_connected(graph):
    visited = set()
    queue = [0]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue += graph[node]

    return len(visited) == len(graph)

# Check if the graph is a bus by checking if all nodes are connected to at least two other nodes
def is_bus(graph):
    for node in range(len(graph)):
        if len(graph[node]) < 2:
            return False
    return True

# Check if the graph is a ring by checking if all nodes are connected to exactly two other nodes
def is_ring(graph):
    for node in range(len(graph)):
        if len(graph[node]) != 2:
            return False
    return True

# Check if the graph is a star by checking if there is a single central node that is connected to all other nodes
def is_star(graph):
    central_node = None
    for node in range(len(graph)):
        if len(graph[node]) == len(graph) - 1:
            if central_node is not None:
                return False
            central_node = node
    return central_node is not None

