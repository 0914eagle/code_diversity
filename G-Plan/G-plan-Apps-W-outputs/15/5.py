
def remove_sad_leaves(n, vertices, edges):
    tree = {}
    for i in range(1, n + 1):
        tree[i] = {'value': vertices[i - 1], 'children': []}

    for p, c in edges:
        tree[p]['children'].append((c, tree[p]['value']))

    def dfs(node):
        max_distance = 0
        for child, edge_value in tree[node]['children']:
            child_distance = dfs(child) + edge_value
            max_distance = max(max_distance, child_distance)
        return max_distance

    def remove_leaves(node, max_distance):
        if max_distance > tree[node]['value']:
            return 1
        removed_leaves = 0
        for child, _ in tree[node]['children']:
            removed_leaves += remove_leaves(child, max_distance)
        return removed_leaves

    max_distance_root = dfs(1)
    removed_leaves_count = remove_leaves(1, max_distance_root)
    return removed_leaves_count

if __name__ == "__main__":
    n = int(input())
    vertices = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    print(remove_sad_leaves(n, vertices, edges))
