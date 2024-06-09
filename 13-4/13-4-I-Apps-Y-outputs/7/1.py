
def solve(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(n):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # Initialize a set to store the connected components
    connected_components = set()
    
    # Iterate through the graph and find the connected components
    for node in graph:
        if node not in connected_components:
            # DFS to find all the connected components
            dfs(graph, node, connected_components)
    
    # Initialize a set to store the cycles
    cycles = set()
    
    # Iterate through the connected components and find the cycles
    for component in connected_components:
        if len(component) > 2:
            # Check if the component is a cycle
            if is_cycle(graph, component):
                cycles.add(component)
    
    return len(cycles)

def dfs(graph, node, connected_components):
    # Mark the current node as visited
    connected_components.add(node)
    
    # Recursively explore the graph
    for neighbor in graph[node]:
        if neighbor not in connected_components:
            dfs(graph, neighbor, connected_components)

def is_cycle(graph, component):
    # Check if the component is a cycle
    for node in component:
        for neighbor in graph[node]:
            if neighbor not in component:
                return False
    return True

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v = map(int, input().split())
    edges.append([u, v])
print(solve(n, m, edges))

