
def solve(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(edges[i + 1] - 1)

    # Initialize the color of the root vertex as 1
    color = 1
    visited = [False] * n
    visited[0] = True

    # BFS to color the tree
    queue = [0]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                color = colors[neighbor]
        for neighbor in graph[vertex]:
            if colors[neighbor] == 0:
                colors[neighbor] = color

    # Count the number of steps needed to color the tree
    steps = 0
    for i in range(n):
        if colors[i] != 0:
            steps += 1

    return steps

