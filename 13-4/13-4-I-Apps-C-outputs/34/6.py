
def solve(n, m, s, edges):
    # Initialize the graph as an adjacency list
    graph = [[] for _ in range(n + 1)]
    for edge in edges:
        u, v = edge[1], edge[2]
        graph[u].append(v)
        graph[v].append(u)

    # Find all reachable vertices from vertex s
    visited = [False] * (n + 1)
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        if not visited[vertex]:
            visited[vertex] = True
            queue.extend(graph[vertex])

    # Create two plans: one to maximize and one to minimize the number of reachable vertices
    plan_max = []
    plan_min = []
    for edge in edges:
        u, v = edge[1], edge[2]
        if edge[0] == 1:  # directed edge
            plan_max.append('+')
            plan_min.append('+')
        else:  # undirected edge
            if visited[u] and visited[v]:  # both vertices are reachable
                plan_max.append('+')
                plan_min.append('-')
            else:  # at least one vertex is not reachable
                plan_max.append('-')
                plan_min.append('+')

    return len(plan_max), "".join(plan_max), len(plan_min), "".join(plan_min)

