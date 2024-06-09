
def count_cycles(n, m, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        u, v = edge
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    
    # Initialize a visited array and a component array
    visited = [False] * n
    components = []
    
    # Iterate through all vertices
    for vertex in range(n):
        if not visited[vertex]:
            # If the vertex is not visited, start a new component
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)
    
    # Count the number of components that are also cycles
    cycle_count = 0
    for component in components:
        if len(component) > 2 and is_cycle(graph, component):
            cycle_count += 1
    
    return cycle_count

def dfs(graph, vertex, visited, component):
    # Mark the current vertex as visited
    visited[vertex] = True
    # Add the current vertex to the component
    component.append(vertex)
    # Recursively explore the neighbors of the current vertex
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def is_cycle(graph, component):
    # Check if the component is a cycle by checking if all edges are distinct
    edges = set()
    for i in range(len(component)):
        for j in range(i + 1, len(component)):
            if component[i] in graph[component[j]]:
                return False
            edges.add((component[i], component[j]))
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(count_cycles(n, m, edges))

