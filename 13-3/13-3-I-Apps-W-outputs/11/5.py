
def solve(n, x):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # Find the leaf nodes in the graph
    leaf_nodes = []
    for i in range(n):
        if len(graph[i]) <= 1:
            leaf_nodes.append(i)

    # Check if the special node x is a leaf node
    if x in leaf_nodes:
        return "Ashish"

    # Check if Ayush can remove the special node x in his first move
    for i in range(n):
        if x in graph[i]:
            return "Ayush"

    # Check if Ashish can remove the special node x in his first move
    for i in range(n):
        if x in graph[i] and i not in leaf_nodes:
            return "Ashish"

    # If both players cannot remove the special node x in their first move, then the game is a draw
    return "Draw"

