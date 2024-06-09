
def solve(n, pleasantness, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the root of the tree (the gift with no incoming edges)
    root = 0
    for i in range(n):
        if not graph[i]:
            root = i
            break

    # Initialize the maximum sum of pleasantness as 0
    max_sum = 0

    # Recursively explore the tree and find the maximum sum of pleasantness
    def dfs(node, parent, sum):
        nonlocal max_sum
        # If the current node is the root, return the current sum
        if node == root:
            max_sum = max(max_sum, sum)
            return
        # If the current node has no children, return the current sum
        if not graph[node]:
            max_sum = max(max_sum, sum)
            return
        # Recursively explore the children of the current node
        for child in graph[node]:
            if child != parent:
                dfs(child, node, sum + pleasantness[node])

    # Start the recursion from the root node
    dfs(root, -1, 0)

    # Return the maximum sum of pleasantness
    return max_sum

