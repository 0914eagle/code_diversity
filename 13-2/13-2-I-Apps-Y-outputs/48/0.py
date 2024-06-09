
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
        # If the vertex has not been visited, explore it
        if vertex not in visited:
            # Explore the graph recursively starting from the current vertex
            explore_graph(graph, vertex, visited)
            num_cycles += 1
    
    return num_cycles

def explore_graph(graph, vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)
    
    # Iterate over the neighbors of the current vertex
    for neighbor in graph[vertex]:
        # If the neighbor has not been visited, explore it
        if neighbor not in visited:
            explore_graph(graph, neighbor, visited)

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_cycles(n, m, edges))

