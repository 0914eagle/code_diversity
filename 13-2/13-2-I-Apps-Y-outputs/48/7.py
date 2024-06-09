
def find_cycles(n, m, edges):
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
            # DFS to find the connected component
            connected_component = set()
            dfs(graph, node, connected_component)
            connected_components.add(frozenset(connected_component))
    
    # Initialize a set to store the cycles
    cycles = set()
    
    # Iterate through the connected components and find the cycles
    for connected_component in connected_components:
        if len(connected_component) > 2:
            # Check if the connected component is a cycle
            cycle = check_cycle(graph, connected_component)
            if cycle:
                cycles.add(frozenset(cycle))
    
    return len(cycles)

def dfs(graph, node, connected_component):
    connected_component.add(node)
    for neighbor in graph[node]:
        if neighbor not in connected_component:
            dfs(graph, neighbor, connected_component)

def check_cycle(graph, connected_component):
    # Check if the connected component is a cycle
    for node in connected_component:
        for neighbor in graph[node]:
            if neighbor not in connected_component:
                return False
    return list(connected_component)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append([u, v])
    print(find_cycles(n, m, edges))

