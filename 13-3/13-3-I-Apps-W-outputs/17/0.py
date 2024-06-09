
def solve(n, m, a):
    # Initialize the graph with the given weights
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = a[i - 1]

    # Fill in the rest of the graph with the given weights
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[i][j] = graph[j][i] = a[i - 1] + a[j - 1]

    # Find the minimum spanning tree
    parent = [0] * (n + 1)
    key = [float("inf")] * (n + 1)
    key[1] = 0
    mst = []
    for i in range(1, n + 1):
        min_key = float("inf")
        min_index = 0
        for j in range(1, n + 1):
            if key[j] < min_key:
                min_key = key[j]
                min_index = j
        parent[min_index] = 1
        mst.append((min_index, min_key))
        for j in range(1, n + 1):
            if graph[min_index][j] < key[j]:
                key[j] = graph[min_index][j]
                parent[j] = min_index

    # Find the chains
    chains = []
    for i in range(1, n + 1):
        if parent[i] != 0:
            chains.append((parent[i], i))

    # Check if the number of chains is correct
    if len(chains) != m:
        return -1

    # Return the minimum total cost
    return sum(graph[u][v] for u, v in chains)

