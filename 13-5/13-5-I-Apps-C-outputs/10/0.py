
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n buildings as nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the connections
    for x, y, cost in connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Initialize the minimum spanning tree with the first building as the root
    mst = [0]
    visited = [False] * n
    visited[0] = True

    # Loop through the remaining buildings and add them to the MST
    for i in range(1, n):
        # Find the building with the minimum cost to connect to the MST
        min_cost = float("inf")
        min_index = 0
        for j in range(n):
            if not visited[j] and graph[j][0][1] < min_cost:
                min_cost = graph[j][0][1]
                min_index = j

        # Add the building to the MST and mark it as visited
        mst.append(min_index)
        visited[min_index] = True

    # Check if all insecure buildings are connected to the MST
    for building in insecure_buildings:
        if not visited[building - 1]:
            return "impossible"

    # Calculate the total cost of the MST
    total_cost = 0
    for i in range(1, n):
        total_cost += graph[mst[i]][0][1]

    return total_cost

