
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
    
    # Initialize a set to store the visited vertices
    visited = set()
    
    # Initialize a counter for the number of cycles
    num_cycles = 0
    
    # Iterate over the vertices in the graph
    for vertex in graph:
        # If the vertex has not been visited, explore its connected component
        if vertex not in visited:
            cycle = []
            explore_component(graph, vertex, visited, cycle)
            # If the connected component is a cycle, increment the counter
            if len(cycle) > 2:
                num_cycles += 1
    
    return num_cycles

def explore_component(graph, vertex, visited, cycle):
    # Mark the current vertex as visited
    visited.add(vertex)
    # Add the current vertex to the cycle
    cycle.append(vertex)
    # Iterate over the neighbors of the current vertex
    for neighbor in graph[vertex]:
        # If the neighbor has not been visited, explore its connected component
        if neighbor not in visited:
            explore_component(graph, neighbor, visited, cycle)
    # If the current vertex is not the starting vertex of the cycle, remove it from the cycle
    if vertex != cycle[0]:
        cycle.remove(vertex)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    print(find_cycles(n, m, edges))

