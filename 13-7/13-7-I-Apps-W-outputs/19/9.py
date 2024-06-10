
def get_remote_planets(num_planets, tunnels):
    # Initialize a graph with the given number of planets
    graph = [[] for _ in range(num_planets)]

    # Add edges to the graph based on the tunnels
    for u, v in tunnels:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Find all connected components in the graph
    visited = [False] * num_planets
    connected_components = []
    for i in range(num_planets):
        if not visited[i]:
            component = []
            dfs(graph, i, visited, component)
            connected_components.append(component)

    # A planet is remote if it is in a connected component with only one planet
    remote_planets = 0
    for component in connected_components:
        if len(component) == 1:
            remote_planets += 1

    return remote_planets

def dfs(graph, start, visited, component):
    visited[start] = True
    component.append(start)
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def main():
    num_planets = int(input())
    tunnels = []
    for _ in range(num_planets - 1):
        u, v = map(int, input().split())
        tunnels.append((u, v))
    print(get_remote_planets(num_planets, tunnels))

if __name__ == '__main__':
    main()

