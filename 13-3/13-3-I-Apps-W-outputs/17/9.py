
def solve(n, m, a):
    # Initialize the graph with the given weights
    graph = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i].append((j, a[i - 1] + a[j - 1]))
    
    # Find the minimum spanning tree
    tree = []
    visited = set()
    queue = [(0, 1)]
    while queue:
        parent, node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            tree.append((parent, node))
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((node, neighbor))
    
    # Check if the tree has m - 1 edges
    if len(tree) != m - 1:
        return -1
    
    # Find the minimum total cost
    total_cost = 0
    for parent, node in tree:
        total_cost += graph[parent][node - 1][1]
    
    # Return the minimum total cost and the edges of the minimum spanning tree
    return total_cost, tree

