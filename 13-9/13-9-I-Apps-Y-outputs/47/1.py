
def max_cost_tree(n, a, edges):
    # Initialize a dictionary to store the distance of each node from the root
    dist = {}
    # Initialize a dictionary to store the maximum cost of each subtree
    subtree_max_cost = {}
    # Initialize the root node
    root = 1
    # Calculate the distance of each node from the root
    for i in range(n):
        if i == root:
            dist[i] = 0
        else:
            dist[i] = float('inf')
    # Calculate the maximum cost of each subtree
    for edge in edges:
        u, v = edge
        dist[v] = min(dist[v], dist[u] + 1)
        subtree_max_cost[v] = max(subtree_max_cost.get(v, 0), a[v])
        subtree_max_cost[u] = max(subtree_max_cost.get(u, 0), a[u])
    # Calculate the maximum cost of the entire tree
    max_cost = 0
    for i in range(n):
        max_cost += dist[i] * subtree_max_cost[i]
    return max_cost

