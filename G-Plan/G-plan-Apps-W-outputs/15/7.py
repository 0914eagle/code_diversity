
def remove_sad_leaves(n, vertex_values, edges):
    tree = {}
    for p, c in edges:
        if p not in tree:
            tree[p] = []
        tree[p].append(c)

    def dfs(node):
        if node not in tree:
            return 0
        max_dist = max(dfs(child) + value for child, value in tree[node])
        return max_dist

    sad_vertices = set()
    for i in range(1, n+1):
        if vertex_values[i-1] < dfs(i):
            sad_vertices.add(i)

    leaves_removed = 0
    while sad_vertices:
        leaf = sad_vertices.pop()
        parent = None
        for p, c in edges:
            if p == leaf:
                parent = c
                break
        if parent:
            tree[parent] = [(child, value) for child, value in tree[parent] if child != leaf]
            if not any(child in sad_vertices for child, _ in tree[parent]):
                sad_vertices.discard(parent)
        leaves_removed += 1

    return leaves_removed

if __name__ == "__main__":
    n = int(input())
    vertex_values = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n-1)]

    result = remove_sad_leaves(n, vertex_values, edges)
    print(result)
