
def solve(n, x, edges):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # Initialize the winner as None
    winner = None

    # Iterate through the nodes in the graph
    for node in range(n):
        # If the current node is the special node, set the winner to Ashish
        if node == x-1:
            winner = "Ashish"
            break
        # If the current node is a leaf node, set the winner to Ayush
        if len(graph[node]) <= 1:
            winner = "Ayush"
            break

    return winner

