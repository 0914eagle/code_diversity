
def find_cycles(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    # Find all connected components
    visited = [False] * n
    components = []
    for i in range(n):
        if not visited[i]:
            component = []
            dfs(graph, i, visited, component)
            components.append(component)
    
    # Find all cycles
    cycles = []
    for component in components:
        if len(component) > 2:
            cycle = []
            for i in range(len(component)):
                u = component[i]
                v = component[(i + 1) % len(component)]
                if u in graph[v]:
                    cycle.append(u)
                    cycle.append(v)
            if len(cycle) > 0:
                cycles.append(cycle)
    
    return len(cycles)

def dfs(graph, node, visited, component):
    if visited[node]:
        return
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        dfs(graph, neighbor, visited, component)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_cycles(n, m, edges))

