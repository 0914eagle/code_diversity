_nodes_in_tree(n, edges):
    graph = {}
    for a, b, c in edges:
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = c
        graph[b][a] = c

    def is_rainbow_path(node, parent_color):
        if parent_color is not None and graph[node][parent] == parent_color:
            return False
        for neighbor in graph[node]:
            if neighbor != parent:
                if not is_rainbow_path(neighbor, graph[node][neighbor]):
                    return False
        return True

    def dfs(node, parent):
        if is_rainbow_path(node, None):
            good_nodes.add(node)
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node)

    good_nodes = set()
    dfs(1, None)

    return len(good_nodes), sorted(list(good_nodes))


if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    k, good_nodes = good_nodes_in_tree(n, edges)
    print(k)
    for node in good_nodes:
        print(node