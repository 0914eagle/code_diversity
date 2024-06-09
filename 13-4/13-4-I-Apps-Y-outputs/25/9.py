
def solve(n, edges):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the maximum number of edges in a simple path between three vertices
    max_edges = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                edges_in_path = 0
                visited = set()
                queue = [i, j, k]
                while queue:
                    vertex = queue.pop(0)
                    if vertex not in visited:
                        visited.add(vertex)
                        edges_in_path += len(graph[vertex])
                        queue.extend(graph[vertex])
                max_edges = max(max_edges, edges_in_path)

    # Find the vertices that form the maximum number of edges in a simple path
    vertices = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                edges_in_path = 0
                visited = set()
                queue = [i, j, k]
                while queue:
                    vertex = queue.pop(0)
                    if vertex not in visited:
                        visited.add(vertex)
                        edges_in_path += len(graph[vertex])
                        queue.extend(graph[vertex])
                if edges_in_path == max_edges:
                    vertices.append([i, j, k])

    return vertices[0]

