
def get_unused_switches(n, m, cables):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the cables
    for a, b, length in cables:
        graph[a - 1].append((b - 1, length))
        graph[b - 1].append((a - 1, length))

    # Find all reachable vertices from switch 1
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor, _ in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # Find all unused switches
    unused_switches = []
    for switch in range(n):
        if switch == 0 or switch == n - 1:
            continue
        if not visited[switch]:
            unused_switches.append(switch + 1)

    return len(unused_switches), sorted(unused_switches)

