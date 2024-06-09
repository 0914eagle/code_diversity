
def solve(n, x):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for i in range(n-1):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # Initialize the winner as Ayush
    winner = "Ayush"

    # Loop through each node and check if it is a leaf node
    for node in range(n):
        if len(graph[node]) == 1:
            # If the node is a leaf node, check if it is the special node
            if node+1 == x:
                # If the node is the special node, set the winner to Ashish
                winner = "Ashish"
                break
            else:
                # If the node is not the special node, remove it from the graph
                graph[node].pop()
                graph[graph[node][0]].remove(node)

    return winner

