
def get_maximum_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Initialize variables to store the maximum number of edges and the vertices with the maximum number of edges
    max_edges = 0
    vertices = []
    
    # Iterate over all possible pairs of vertices
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            # Check if there is a path between the two vertices
            if graph[i] and graph[j]:
                # Get the number of edges in the path
                num_edges = len(get_path(graph, i, j))
                # If the number of edges is greater than the maximum, update the maximum and the vertices with the maximum number of edges
                if num_edges > max_edges:
                    max_edges = num_edges
                    vertices = [i, j]
    
    return [max_edges, vertices]

def get_path(graph, start, end):
    # Initialize a queue to store the vertices to visit
    queue = [start]
    # Initialize a set to store the visited vertices
    visited = set()
    
    # Loop until the queue is empty
    while queue:
        # Get the first vertex from the queue
        vertex = queue.pop(0)
        # If the vertex is the end vertex, return the path
        if vertex == end:
            path = []
            while vertex != start:
                path.append(vertex)
                vertex = graph[vertex][0]
            return path[::-1]
        # If the vertex has not been visited, mark it as visited and add its neighbors to the queue
        if vertex not in visited:
            visited.add(vertex)
            queue += graph[vertex]
    
    # If no path is found, return an empty list
    return []

n = 8
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [4, 6], [3, 7], [3, 8]]
print(get_maximum_edges(n, edges))

