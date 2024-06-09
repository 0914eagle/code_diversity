
def solve(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(edges[i + 1] - 1)

    # Initialize the color of the root vertex as 1
    color = 1
    visited = [False] * n
    queue = [0]
    visited[0] = True

    # Breadth-first search to color the tree
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                color = colors[neighbor]
        colors[vertex] = color

    # Return the minimum number of steps required to color the tree
    return len(set(colors))

