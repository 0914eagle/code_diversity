
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
        # Remove the edge from the graph
        graph[edge[0]].remove(edge[1])
        graph[edge[1]].remove(edge[0])

        # Check if the graph is still connected
        if not is_connected(graph):
            bridges += 1

        # Add the edge back to the graph
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return bridges

def is_connected(graph):
    # Initialize a queue to do BFS
    queue = [1]

    # Keep track of the visited vertices
    visited = set()

    # Do BFS until the queue is empty
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])

    # If all vertices are visited, the graph is connected
    return len(visited) == len(graph)

edges = [[1, 3], [2, 7], [3, 4], [4, 5], [4, 6], [5, 6], [6, 7]]
n, m = 7, 7
print(get_bridges(n, m, edges))

