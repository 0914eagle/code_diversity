
def solve(N, roads):
    # Initialize a graph with N junctions
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for u, v in roads:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Count the number of optimal paths of length 2
    count = 0
    for u in range(N):
        for v in range(u + 1, N):
            if len(graph[u]) == 2 and len(graph[v]) == 2:
                count += 1

    return count

