
def remove_sad_leaves(n, vertices, edges):
    tree = {}
    for i in range(1, n + 1):
        tree[i] = {
            'value': vertices[i - 1],
            'children': []
        }

    for p, c in edges:
        tree[p]['children'].append((p + 1, c))

    def dfs(node):
        if not tree[node]['children']:
            return 0, 0

        max_dist = 0
        total_leaves_removed = 0

        for child, dist in tree[node]['children']:
            child_max, child_removed = dfs(child)
            max_dist = max(max_dist, child_max + dist)
            total_leaves_removed += child_removed

        if max_dist > tree[node]['value']:
            total_leaves_removed += 1

        return max_dist, total_leaves_removed

    _, leaves_removed = dfs(1)
    return leaves_removed

if __name__ == "__main__":
    n = int(input())
    vertices = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

    print(remove_sad_leaves(n, vertices, edges))
