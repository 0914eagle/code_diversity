
def get_network_topology(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}

    # Add nodes to the graph
    for i in range(1, n + 1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

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

# Check if the graph is connected
def is_connected(graph):
    visited = set()
    queue = [1]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

    return len(visited) == len(graph)

# Check if the graph is a bus
def is_bus(graph):
    for node in graph:
        if len(graph[node]) != 2:
            return False
    return True

# Check if the graph is a ring
def is_ring(graph):
    for node in graph:
        if len(graph[node]) != 2:
            return False
    return True

# Check if the graph is a star
def is_star(graph):
    central_node = None
    for node in graph:
        if len(graph[node]) == 1:
            if central_node is not None:
                return False
            central_node = node
    return central_node is not None

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(get_network_topology(n, m, edges))

if __name__ == "__main__":
    main()

