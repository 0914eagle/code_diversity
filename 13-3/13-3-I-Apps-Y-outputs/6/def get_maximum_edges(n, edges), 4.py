
def get_maximum_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []

    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # Initialize variables to store the maximum number of edges and the corresponding vertices
    max_edges = 0
    a, b, c = 0, 0, 0

    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Find the path between the two vertices
            path = find_path(graph, i, j)

            # If the path is not empty, check if it is the maximum
            if path:
                if len(path) > max_edges:
                    max_edges = len(path)
                    a, b, c = i, j, 0

    return max_edges, a, b, c

def find_path(graph, start, end):
    # Initialize a queue to store the vertices to visit
    queue = [start]

    # Initialize a set to store the visited vertices
    visited = set()

    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        vertex = queue.pop(0)

        # If the current vertex is the end vertex, return the path
        if vertex == end:
            return queue

        # If the current vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]

    # If the queue is empty, there is no path between the start and end vertices
    return []

n = 8
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (3, 7), (3, 8)]
max_edges, a, b, c = get_maximum_edges(n, edges)
print(max_edges)
print(a, b, c)

