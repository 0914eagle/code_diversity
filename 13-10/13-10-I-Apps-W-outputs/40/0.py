
def get_maximum_dominoes(graph):
    # Initialize a dictionary to store the number of dominoes that can be placed on each vertex
    num_dominoes = {}
    
    # Iterate over the edges in the graph
    for edge in graph:
        # Get the two vertices that the edge connects
        vertex1, vertex2 = edge
        
        # If the vertex is not already in the dictionary, initialize its value to 0
        if vertex1 not in num_dominoes:
            num_dominoes[vertex1] = 0
        if vertex2 not in num_dominoes:
            num_dominoes[vertex2] = 0
        
        # Increment the value of the vertex that is not the endpoint of the edge
        if vertex1 != vertex2:
            num_dominoes[vertex1] += 1
        else:
            num_dominoes[vertex2] += 1
    
    # Return the maximum number of dominoes that can be placed on the edges of the graph
    return max(num_dominoes.values())

def main():
    # Read the number of vertices and edges in the graph
    n, m = map(int, input().split())
    
    # Initialize a list to store the edges of the graph
    graph = []
    
    # Read the edges of the graph
    for _ in range(m):
        edge = tuple(map(int, input().split()))
        graph.append(edge)
    
    # Get the maximum number of dominoes that can be placed on the edges of the graph
    max_dominoes = get_maximum_dominoes(graph)
    
    # Print the maximum number of dominoes
    print(max_dominoes)

if __name__ == '__main__':
    main()

