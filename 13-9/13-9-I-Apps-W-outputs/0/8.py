
def dfs(graph, node, visited, parent, depth):
    visited[node] = True
    depth[node] = depth[parent] + 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, node, depth)

def build_tree(n, k, a):
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    depth = [0] * (n + 1)
    dfs(graph, 1, visited, 0, depth)
    nodes = sorted(range(1, n + 1), key=lambda x: depth[x])
    return nodes[:k], a[nodes[:k]]

def solve(n, k, a):
    nodes, times = build_tree(n, k, a)
    return min(times)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve(n, k, a))

