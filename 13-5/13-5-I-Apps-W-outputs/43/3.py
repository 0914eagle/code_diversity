
def get_minimum_steps(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(edges[i + 1] - 1)

    # Initialize the colors of the vertices
    color = [0] * n
    for i in range(n):
        color[i] = colors[i]

    # Initialize the number of steps to 0
    steps = 0

    # Iterate through all vertices and color them
    for i in range(n):
        # If the vertex has not been colored, color it with the next available color
        if color[i] == 0:
            color[i] = 1
            steps += 1
            # Recursively color the subtree of the vertex
            color_subtree(graph, color, i, steps)

    return steps

def color_subtree(graph, color, vertex, steps):
    # Color the current vertex with the next available color
    color[vertex] += 1
    steps += 1
    # Recursively color the subtree of the vertex
    for neighbor in graph[vertex]:
        if color[neighbor] == 0:
            color_subtree(graph, color, neighbor, steps)

n = 7
edges = [1, 1, 2, 3, 1, 4]
colors = [3, 3, 1, 1, 1, 2, 3]
print(get_minimum_steps(n, edges, colors))

