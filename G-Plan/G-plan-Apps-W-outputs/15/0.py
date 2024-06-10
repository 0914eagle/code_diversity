
def remove_leaves(n, values, edges):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = {'value': values[i - 1], 'children': []}

    for p, c in edges:
        graph[p]['children'].append((c, graph[p]['value']))

    def dfs(node):
        max_distance = 0
        for child, edge_value in graph[node]['children']:
            child_distance = dfs(child) + edge_value
            max_distance = max(max_distance, child_distance)
        return max_distance

    def remove_sad_vertices(node):
        if not graph[node]['children']:
            return 1 if graph[node]['value'] < 0 else 0

        total_removed = 0
        for child, edge_value in graph[node]['children']:
            child_distance = dfs(child) + edge_value
            if child_distance > graph[child]['value']:
                total_removed += remove_sad_vertices(child)
        return total_removed

    return remove_sad_vertices(1)

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    print(remove_leaves(n, values, edges))
