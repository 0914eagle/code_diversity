
def is_reasonable_network(n, m, friends):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(m):
        graph[friends[i][0] - 1].append(friends[i][1])
        graph[friends[i][1] - 1].append(friends[i][0])

    # Check if the network is reasonable
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and i != k:
                    if (j in graph[i] and k in graph[j]) and (k not in graph[i]):
                        return "NO"

    return "YES"

