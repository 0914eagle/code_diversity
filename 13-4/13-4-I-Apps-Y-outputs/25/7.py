
def get_maximum_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize three variables to store the maximum number of edges and the vertices corresponding to the maximum number of edges
    max_edges = 0
    max_vertices = []
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # If the vertices are not already in the maximum set, calculate the number of edges in the simple path between them
            if i not in max_vertices and j not in max_vertices:
                num_edges = count_edges(graph, i, j)
                # If the number of edges is greater than the current maximum, update the maximum and the corresponding vertices
                if num_edges > max_edges:
                    max_edges = num_edges
                    max_vertices = [i, j]
    
    return max_edges, max_vertices

def count_edges(graph, i, j):
    # Initialize a set to store the vertices in the simple path between i and j
    visited = set()
    # Initialize a queue to store the vertices to be visited
    queue = [i]
    # Initialize a counter to store the number of edges in the simple path
    count = 0
    
    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.pop(0)
        # If the vertex is not already in the visited set, add it to the visited set and increment the counter
        if vertex not in visited:
            visited.add(vertex)
            count += 1
        # If the vertex is the destination vertex, return the counter
        if vertex == j:
            return count
        # Enqueue the neighbors of the vertex that are not already in the visited set
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return count

n = 8
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (4, 6), (3, 7), (3, 8)]
max_edges, max_vertices = get_maximum_edges(n, edges)
print(max_edges)
print(max_vertices)

