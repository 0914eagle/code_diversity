
def solve(n, m, edges):
    # Initialize a dictionary to store the edges
    graph = {}

    # Iterate over the edges and add them to the dictionary
    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        if v not in graph:
            graph[v] = []
        graph[v].append(u)

    # Initialize a set to store the visited vertices
    visited = set()

    # Initialize a queue to store the vertices to be visited
    queue = [1]

    # Iterate while the queue is not empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)

        # If the vertex has not been visited before, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]

    # If all vertices have been visited, return "Yes" and the corresponding string
    if len(visited) == n:
        string = "a" * (n - 1) + "c"
        return "Yes\n" + string

    # Otherwise, return "No"
    return "No"

