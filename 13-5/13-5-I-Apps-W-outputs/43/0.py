
def get_minimum_steps(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(edges[i + 1] - 1)

    # Initialize the color of the root vertex as 1
    color = 1
    visited = [False] * n
    queue = [0]
    visited[0] = True

    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                color = colors[neighbor]
        colors[vertex] = color

    # Count the number of steps
    steps = 0
    for i in range(n):
        if colors[i] != colors[edges[i] - 1]:
            steps += 1

    return steps

