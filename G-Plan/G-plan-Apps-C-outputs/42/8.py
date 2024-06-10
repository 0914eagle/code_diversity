
def find_good_nodes(n, edges):
    graph = {}
    for a, b, c in edges:
        if a not in graph:
            graph[a] = {}
        if b not in graph:
            graph[b] = {}
        graph[a][b] = c
        graph[b][a] = c

    def is_rainbow_path(node, parent, colors):
        if parent is not None and colors[node] == colors[parent]:
            return False
        for neighbor in graph[node]:
            if neighbor != parent:
                if not is_rainbow_path(neighbor, node, colors):
                    return False
        return True

    good_nodes = []
    for node in range(1, n + 1):
        colors = {node: 0}
        for neighbor in graph[node]:
            colors[neighbor] = graph[node][neighbor]
        if is_rainbow_path(node, None, colors):
            good_nodes.append(node)

    return good_nodes

if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    result = find_good_nodes(n, edges)
    print(len(result))
    for node in result:
        print(node)
