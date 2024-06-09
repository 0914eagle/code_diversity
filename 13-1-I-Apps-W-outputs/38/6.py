
def get_maximum_sum(n, pleasantness, edges):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Find the root of the tree (the gift with id 1)
    root = 1
    while root in graph:
        root = graph[root].pop()

    # Initialize the maximum sum of pleasantness as 0
    max_sum = 0

    # Recursively find the maximum sum of pleasantness for Chloe and Vladik
    def dfs(node, parent, sum):
        nonlocal max_sum
        # If the node is the root, return the sum
        if node == root:
            max_sum = max(max_sum, sum)
            return
        # If the node has already been visited, return
        if node in graph[parent]:
            return
        # Add the pleasantness of the current node to the sum
        sum += pleasantness[node - 1]
        # Recursively call the function for each child of the current node
        for child in graph[node]:
            dfs(child, node, sum)

    # Call the dfs function for the root node
    dfs(root, None, 0)

    # Return the maximum sum of pleasantness
    return max_sum

