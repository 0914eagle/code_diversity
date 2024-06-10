
def get_remote_planets(n, tunnels):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for tunnel in tunnels:
        graph[tunnel[0] - 1].append(tunnel[1] - 1)
        graph[tunnel[1] - 1].append(tunnel[0] - 1)

    # Find all connected components in the graph
    visited = [False] * n
    connected_components = []
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(graph, i, visited, component)
            connected_components.append(component)

    # Count the number of remote planets
    remote_planets = 0
    for component in connected_components:
        if len(component) == 1:
            remote_planets += 1

    return remote_planets

def dfs(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

if __name__ == '__main__':
    n = int(input())
    tunnels = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tunnels.append((u, v))
    print(get_remote_planets(n, tunnels))

