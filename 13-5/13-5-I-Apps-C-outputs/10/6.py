
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n buildings as nodes
    graph = [[] for _ in range(n)]

    # Add edges between buildings based on the connections
    for x, y, cost in connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Initialize the minimum spanning tree with the first building as the root
    mst = [0]
    visited = [False] * n
    visited[0] = True

    # Loop through the remaining buildings and add them to the MST
    for i in range(1, n):
        # Find the unvisited building with the minimum cost
        min_cost = float("inf")
        min_index = 0
        for j in range(n):
            if not visited[j] and graph[mst[-1]][j][1] < min_cost:
                min_cost = graph[mst[-1]][j][1]
                min_index = j

        # Add the building to the MST and mark it as visited
        mst.append(min_index)
        visited[min_index] = True

    # Check if the MST satisfies the security measure
    for i in range(n):
        for j in range(n):
            if i != j and graph[i][j][1] < float("inf"):
                path = [i]
                current = j
                while current != i:
                    for neighbor in graph[current]:
                        if neighbor[0] not in path and neighbor[1] < float("inf"):
                            current = neighbor[0]
                            path.append(current)
                            break
                if any(path[i] in insecure_buildings for i in range(1, len(path))):
                    return "impossible"

    # Return the total cost of the MST
    return sum(graph[mst[i - 1]][mst[i]][1] for i in range(1, len(mst)))

