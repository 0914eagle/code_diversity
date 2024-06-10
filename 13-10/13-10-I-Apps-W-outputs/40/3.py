
def max_dominoes(graph):
    
    # Initialize a dictionary to store the number of dominoes for each vertex
    dominoes = {}
    for vertex in graph:
        dominoes[vertex] = 0
    
    # Iterate through the edges of the graph
    for edge in graph.edges:
        # Get the vertices of the edge
        vertex1, vertex2 = edge
        
        # Check if the vertices have the same number of dominoes
        if dominoes[vertex1] == dominoes[vertex2]:
            # Increment the number of dominoes for both vertices
            dominoes[vertex1] += 1
            dominoes[vertex2] += 1
    
    # Return the maximum number of dominoes
    return max(dominoes.values())

def read_data():
    
    # Read the number of vertices and edges
    num_vertices, num_edges = map(int, input().split())
    
    # Initialize a dictionary to represent the graph
    graph = {}
    
    # Read the edges
    for _ in range(num_edges):
        # Read the edge
        edge = tuple(map(int, input().split()))
        
        # Add the edge to the graph
        if edge[0] not in graph:
            graph[edge[0]] = {}
        graph[edge[0]][edge[1]] = 1
        if edge[1] not in graph:
            graph[edge[1]] = {}
        graph[edge[1]][edge[0]] = 1
    
    return graph

if __name__ == '__main__':
    # Read the input data
    graph = read_data()
    
    # Call the max_dominoes function
    max_dominoes = max_dominoes(graph)
    
    # Print the result
    print(max_dominoes)

