
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for t, u, v in edges:
        if t == 1:
            graph[u].append(v)
        else:
            graph[u].append(v)
            graph[v].append(u)
    
    # Find all reachable vertices from vertex s
    reachable = set([s])
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    
    # Find the maximum number of reachable vertices by orienting all undirected edges from vertex s
    max_reachable = len(reachable)
    max_edges = []
    for t, u, v in edges:
        if t == 2 and u == s:
            max_edges.append((u, v))
    
    # Find the minimum number of reachable vertices by orienting all undirected edges from vertex s
    min_reachable = len(reachable)
    min_edges = []
    for t, u, v in edges:
        if t == 2 and u == s:
            min_edges.append((u, v))
    
    # Print the plans
    print(max_reachable)
    print(''.join('+' if edge in max_edges else '-' for edge in edges if edge[0] == s))
    print(min_reachable)
    print(''.join('+' if edge in min_edges else '-' for edge in edges if edge[0] == s))

if __name__ == '__main__':
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        t, u, v = map(int, input().split())
        edges.append((t, u, v))
    solve(n, m, s, edges)

