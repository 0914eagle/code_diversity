
def solve(n, x):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # Check if node x is a leaf node
    if len(graph[x-1]) <= 1:
        return "Ashish"

    # Check if any other node is a leaf node
    for i in range(n):
        if i != x-1 and len(graph[i]) <= 1:
            return "Ayush"

    # If no node is a leaf node, then Ashish wins
    return "Ashish"

