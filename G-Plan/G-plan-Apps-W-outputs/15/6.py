
def remove_leaves(n, vertices, edges):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for p, c in edges:
        graph[p].append(c)

    def dfs(node):
        if not graph[node]:
            return 0

        max_dist = max(dfs(child) + weight for child, weight in graph[node])
        return max_dist

    def is_sad(node):
        return dfs(node) > vertices[node - 1]

    def remove_sad_leaves(node):
        if not graph[node]:
            return 1

        removed_leaves = 0
        for child, _ in graph[node]:
            removed_leaves += remove_sad_leaves(child)

        if is_sad(node):
            removed_leaves += 1

        return removed_leaves

    return remove_sad_leaves(1) - 1

if __name__ == "__main__":
    n = int(input())
    vertices = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]

    print(remove_leaves(n, vertices, edges))
