
import math

def solve(D, q, queries):
    # Initialize a dictionary to store the graph
    graph = {}

    # Build the graph
    for i in range(1, int(math.sqrt(D)) + 1):
        if D % i == 0:
            x = i
            y = D // i
            if x != y:
                graph[x] = graph.get(x, []) + [y]
                graph[y] = graph.get(y, []) + [x]

    # Initialize a dictionary to store the number of shortest paths between two vertices
    paths = {}

    # Iterate over the queries
    for v, u in queries:
        # If the query is for the same vertex, return 1
        if v == u:
            paths[v, u] = 1
            continue

        # If the query is for two different vertices, calculate the number of shortest paths between them
        paths[v, u] = 0
        queue = [(v, 0)]
        visited = set()
        while queue:
            vertex, distance = queue.pop(0)
            if vertex == u:
                paths[v, u] += 1
                continue
            if vertex in visited:
                continue
            visited.add(vertex)
            for neighbor in graph[vertex]:
                queue.append((neighbor, distance + 1))

    # Return the number of shortest paths for each query
    return [paths[v, u] % 998244353 for v, u in queries]

