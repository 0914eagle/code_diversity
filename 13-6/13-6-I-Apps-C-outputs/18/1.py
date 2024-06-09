
def get_unused_switches(n, m, edges):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find all nodes that are not reachable from node 1
    unused_switches = []
    for i in range(n):
        if i == 0:
            continue
        if not dfs(graph, 0, i):
            unused_switches.append(i)

    return len(unused_switches), sorted(unused_switches)

def dfs(graph, start, target):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        if node == target:
            return True
        for neighbor in graph[node]:
            stack.append(neighbor)
    return False

edges = [(1, 2, 2), (1, 3, 1), (1, 4, 3), (2, 6, 1), (2, 7, 2), (3, 5, 1), (4, 7, 2), (5, 7, 1)]
n, m = 7, 8
print(get_unused_switches(n, m, edges))

