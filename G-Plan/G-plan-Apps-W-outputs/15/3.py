
def remove_leaves(n, vertex_values, edges):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for p, c in edges:
        graph[p].append(c)

    def dfs(node):
        if not graph[node]:
            return 0, vertex_values[node - 1]

        max_dist = 0
        total_leaves = 0

        for child in graph[node]:
            child_leaves, child_dist = dfs(child)
            max_dist = max(max_dist, child_dist + 1)
            total_leaves += child_leaves

        if max_dist > vertex_values[node - 1]:
            return total_leaves, max_dist

        return total_leaves + 1, vertex_values[node - 1]

    leaves_removed, _ = dfs(1)
    return leaves_removed

if __name__ == "__main__":
    n = int(input())
    vertex_values = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]

    result = remove_leaves(n, vertex_values, edges)
    print(result)
