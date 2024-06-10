
def remove_leaves(n, values, edges):
    graph = {i: [] for i in range(1, n + 1)}
    for p, c in edges:
        graph[p].append(c)

    def dfs(node):
        if not graph[node]:
            return 0, values[node - 1]
        
        max_dist = 0
        for child in graph[node]:
            dist, val = dfs(child)
            max_dist = max(max_dist, dist + val)
        
        return max_dist, max_dist + values[node - 1]

    def remove_sad_vertices(node):
        if not graph[node]:
            return 1
        
        removed_leaves = 0
        for child in graph[node]:
            removed_leaves += remove_sad_vertices(child)
        
        if removed_leaves > values[node - 1]:
            return 0
        return 1 + removed_leaves

    _, root_dist = dfs(1)
    return n - remove_sad_vertices(1)

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    print(remove_leaves(n, values, edges))
