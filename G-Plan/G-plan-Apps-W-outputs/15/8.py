
def remove_sad_leaves(n, vertices, edges):
    def dfs(vertex, parent, dist):
        max_dist = vertices[vertex - 1]
        for child, edge_dist in edges[vertex]:
            if child != parent:
                max_dist = max(max_dist, dfs(child, vertex, dist + edge_dist))
        return max_dist - dist

    def remove_leaves(vertex, parent, dist):
        nonlocal removed_leaves
        max_dist = vertices[vertex - 1]
        for child, edge_dist in edges[vertex]:
            if child != parent:
                max_dist = max(max_dist, remove_leaves(child, vertex, dist + edge_dist))
        if max_dist - dist > vertices[vertex - 1]:
            removed_leaves += 1
            return dist
        return max_dist

    edges = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        p, c = map(int, input().split())
        edges[i + 2].append((p, c))
        edges[p].append((i + 2, c))

    removed_leaves = 0
    remove_leaves(1, 0, 0)
    return removed_leaves

if __name__ == "__main__":
    n = int(input())
    vertices = list(map(int, input().split()))
    print(remove_sad_leaves(n, vertices, {}))
