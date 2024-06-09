
def get_roads(n, a):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]
    # Add edges to the graph
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j]:
                graph[i].append(j)
                graph[j].append(i)
    # Find all connected components in the graph
    connected_components = []
    for i in range(n):
        if i not in connected_components:
            component = []
            dfs(i, graph, component)
            connected_components.append(component)
    # Check if all connected components have at least 2 nodes
    for component in connected_components:
        if len(component) < 2:
            return "NO"
    # Build roads between connected components
    roads = []
    for i in range(n):
        for j in range(i+1, n):
            if a[i] != a[j] and i not in connected_components[j] and j not in connected_components[i]:
                roads.append([i, j])
    return "YES\n" + "\n".join(str(road[0]) + " " + str(road[1]) for road in roads)

def dfs(node, graph, visited):
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_roads(n, a))

