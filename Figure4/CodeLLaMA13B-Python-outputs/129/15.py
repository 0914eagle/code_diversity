def minPath(grid, k):
    
    # Create a visited matrix to keep track of visited nodes
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Create a matrix to keep track of the minimum path to the node
    dist = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # Initialize the source node
    source = (0, 0)
    visited[source[0]][source[1]] = True
    dist[source[0]][source[1]] = 0

    # Create a queue and enqueue source node
    queue = []
    queue.append(source)

    # Loop to traverse every node
    while queue:
        # Extract the front node from the queue
        u = queue.pop(0)

        # If the front node is the destination node, we are done
        if u[0] == len(grid) - 1 and u[1] == len(grid[0]) - 1:
            break

        # Traverse the four neighbors of the dequeued node
        for v in [(u[0] - 1, u[1]), (u[0] + 1, u[1]), (u[0], u[1] - 1), (u[0], u[1] + 1)]:
            # If the neighbor is a valid cell, is not visited and has a value
            # less than the maximum value of the grid
            if (
                v[0] >= 0
                and v[0] < len(grid)
                and v[1] >= 0
                and v[1] < len(grid[0])
                and not visited[v[0]][v[1]]
                and grid[v[0]][v[1]] < len(grid) * len(grid[0])
            ):
                # Set the distance of the neighbor cell
                dist[v[0]][v[1]] = dist[u[0]][u[1]] + 1
                # Enqueue the neighbor cell
                queue.append(v)
                # Mark the neighbor cell as visited
                visited[v[0