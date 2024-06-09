
def num_cycles(n, m, edges):
    # Initialize a dictionary to store the graph
    graph = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)

    # Initialize a set to store the visited vertices
    visited = set()

    # Initialize a counter for the number of cycles
    num_cycles = 0

    # Iterate over the vertices in the graph
    for vertex in graph:
        # If the vertex has not been visited, explore it
        if vertex not in visited:
            # Explore the graph starting from the current vertex
            explore_graph(graph, vertex, visited)

            # If the current vertex is connected to all other vertices, it is a cycle
            if len(visited) == n:
                num_cycles += 1

    return num_cycles

def explore_graph(graph, vertex, visited):
    # Mark the current vertex as visited
    visited.add(vertex)

    # Explore the neighbors of the current vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            explore_graph(graph, neighbor, visited)

# Test the function with the example input
n = 5
m = 4
edges = [(1, 2), (3, 4), (5, 4), (3, 5)]
print(num_cycles(n, m, edges)) # Output: 1

n = 17
m = 15
edges = [(1, 8), (1, 12), (5, 11), (11, 9), (9, 15), (15, 5), (4, 13), (3, 13), (4, 3), (10, 16), (7, 10), (16, 7), (14, 3), (14, 4), (17, 6)]
print(num_cycles(n, m, edges)) # Output: 2

