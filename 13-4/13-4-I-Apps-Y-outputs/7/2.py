
def num_cycles(n, m, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for edge in edges:
        u, v = edge[0], edge[1]
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize a visited array and a component array
    visited = [False] * n
    components = []

    # Iterate through all vertices in the graph
    for vertex in range(n):
        # If the vertex is not visited, do a DFS traversal and add the connected component to the components array
        if not visited[vertex]:
            component = []
            dfs(graph, vertex, visited, component)
            components.append(component)

    # Initialize a count of cycles
    cycle_count = 0

    # Iterate through all components in the components array
    for component in components:
        # If the component is a cycle, increment the cycle count
        if is_cycle(component):
            cycle_count += 1

    return cycle_count

def dfs(graph, vertex, visited, component):
    # Mark the current vertex as visited
    visited[vertex] = True

    # Add the current vertex to the component array
    component.append(vertex)

    # Iterate through all neighbors of the current vertex
    for neighbor in graph[vertex]:
        # If the neighbor is not visited, do a DFS traversal
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)

def is_cycle(component):
    # If the component is empty, it is not a cycle
    if len(component) == 0:
        return False

    # If the component has only one vertex, it is not a cycle
    if len(component) == 1:
        return False

    # If the component has two vertices, it is a cycle if they are connected
    if len(component) == 2:
        return component[0] in graph[component[1]] and component[1] in graph[component[0]]

    # If the component has three or more vertices, it is a cycle if it forms a cycle with the first and last vertex
    return component[0] in graph[component[-1]] and component[-1] in graph[component[0]]

# Test the function with the given examples
n = 5
m = 4
edges = [[1, 2], [3, 4], [5, 4], [3, 5]]
print(num_cycles(n, m, edges)) # output: 1

n = 17
m = 15
edges = [[1, 8], [1, 12], [5, 11], [11, 9], [9, 15], [15, 5], [4, 13], [3, 13], [4, 3], [10, 16], [7, 10], [16, 7], [14, 3], [14, 4], [17, 6]]
print(num_cycles(n, m, edges)) # output: 2

