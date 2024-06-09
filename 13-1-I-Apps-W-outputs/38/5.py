
def solve(n, pleasantness, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find the root of the tree (the gift that hangs on no other gift)
    root = 0
    for i in range(1, n):
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
        # Otherwise, recursively explore the tree
        for child in graph[node]:
            if child != parent:
                dfs(child, node, sum + pleasantness[child])

    dfs(root, -1, 0)

    # Return the maximum sum of pleasantness
    return max_sum

