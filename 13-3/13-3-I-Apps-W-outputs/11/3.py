
def solve(n, x):
    # Initialize a graph with n nodes and 0 edges
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
        for neighbor in graph[i]:
            degree[i] += 1
            degree[neighbor] += 1

    # Initialize the winner to Ayush
    winner = "Ayush"

    # Loop through each node and check if it is a leaf node
    for i in range(n):
        if degree[i] <= 1:
            # If the node is a leaf node, check if it is the special node
            if i + 1 == x:
                # If it is the special node, the winner is Ashish
                winner = "Ashish"
                break
            else:
                # If it is not the special node, Ayush can remove it in his turn
                winner = "Ayush"
                break

    return winner

