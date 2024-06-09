
def is_reasonable_network(n, m, friends):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges between friends
    for i in range(m):
        graph[friends[i][0] - 1].append(friends[i][1])
        graph[friends[i][1] - 1].append(friends[i][0])

    # Check if the network is transitive
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j and j != k and graph[i][j] and graph[j][k]:
                    if not graph[i][k]:
                        return "NO"

    return "YES"

