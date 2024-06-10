
from collections import defaultdict

def find_good_nodes(n, edges):
    graph = defaultdict(list)
    for a, b, c in edges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def is_rainbow_path(path):
        colors = set()
        for i in range(len(path) - 1):
            colors.add(graph[path[i]][path[i + 1]])
        return len(colors) == len(path) - 1

    def dfs(node, parent, path):
        good_node = True
        for neighbor, color in graph[node]:
            if neighbor != parent:
                if color in path:
                    good_node = False
                    break
                good_node &= dfs(neighbor, node, path + [color])
        if good_node:
            good_nodes.add(node)
        return good_node

    good_nodes = set()
    for i in range(1, n + 1):
        dfs(i, -1, [])
    
    return good_nodes

if __name__ == '__main__':
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    good_nodes = find_good_nodes(n, edges)
    
    print(len(good_nodes))
    for node in sorted(good_nodes):
        print(node)
