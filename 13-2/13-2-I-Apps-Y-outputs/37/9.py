
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
        # Remove the edge and check if the graph is still connected
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])
        if not is_connected(graph):
            bridges.append(edge)
        # Add the edge back to the graph
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return len(bridges)

def is_connected(graph):
    # Initialize a queue to do BFS
    queue = [1]

    # Keep track of the visited vertices
    visited = set()

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])

    return len(visited) == len(graph)

edges = []
for i in range(m):
    edges.append([int(x) for x in input().split()])

print(get_bridges(n, m, edges))

