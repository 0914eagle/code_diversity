
def get_minimum_steps(n, edges, colors):
    # Create a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        graph[edges[i] - 1].append(i + 1)

    # Initialize the color of the root vertex as 0
    color = [0] * n
    color[0] = 1

    # Queue to store the vertices to be colored
    queue = [0]

    # Loop until the queue is empty
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)

        # Get the color of the current vertex
        current_color = color[vertex]

        # Loop through the neighbors of the current vertex
        for neighbor in graph[vertex]:
            # If the neighbor has not been colored, color it with the current color
            if color[neighbor] == 0:
                color[neighbor] = current_color
                queue.append(neighbor)
            # If the neighbor has been colored with a different color, return -1
            elif color[neighbor] != current_color:
                return -1

    # Loop through the colors and count the number of vertices with each color
    count = [0] * (max(colors) + 1)
    for c in colors:
        count[c] += 1

    # Return the minimum number of steps required to color the tree
    return min(count)

