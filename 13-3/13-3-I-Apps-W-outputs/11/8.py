
def solve(n, x):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n - 1):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize the degree of each node to 0
    degree = [0] * n

    # Count the degree of each node
    for i in range(n):
        for j in graph[i]:
            degree[i] += 1
            degree[j] += 1

    # If the degree of node x is 1, Ayush wins
    if degree[x - 1] == 1:
        return "Ayush"

    # If the degree of node x is not 1, Ashish wins
    return "Ashish"

