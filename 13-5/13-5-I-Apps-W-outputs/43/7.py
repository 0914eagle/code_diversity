
def get_minimum_steps(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(edges[i + 1] - 1)

    # Initialize the color of the root vertex as 0
    color = [0] * n

    # Queue for BFS
    queue = [0]

    # Step counter
    steps = 0

    while queue:
        # BFS
        for _ in range(len(queue)):
            vertex = queue.pop(0)
            for neighbor in graph[vertex]:
                if color[neighbor] == 0:
                    color[neighbor] = colors[vertex]
                    queue.append(neighbor)

        # Increment the step counter
        steps += 1

    return steps

