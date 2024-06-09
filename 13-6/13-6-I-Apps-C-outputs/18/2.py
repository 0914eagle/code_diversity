
def get_unused_switches(n, m, cables):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for a, b, length in cables:
        graph[a - 1].append((b - 1, length))
        graph[b - 1].append((a - 1, length))
    
    # Find all nodes that are not reachable from node 0 (switch 1)
    unused_switches = []
    visited = [False] * n
    queue = [0]
    while queue:
        node = queue.pop(0)
        if not visited[node]:
            visited[node] = True
            for neighbor, length in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
    
    for i in range(n):
        if i != 0 and not visited[i]:
            unused_switches.append(i + 1)
    
    return len(unused_switches), sorted(unused_switches)

