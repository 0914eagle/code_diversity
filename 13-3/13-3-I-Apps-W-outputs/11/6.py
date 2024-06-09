
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

    # If the special node x is a leaf node, return "Ashish"
    if degree[x - 1] <= 1:
        return "Ashish"

    # If the special node x is not a leaf node, return "Ayush"
    return "Ayush"

