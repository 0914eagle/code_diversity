
def get_niceness(graph):
    # Initialize the niceness of the graph as 0
    niceness = 0
    
    # Iterate over all possible colorings of the graph
    for coloring in itertools.product([0, 1], repeat=len(graph)):
        # Get the distances between white and black vertices
        white_distances = get_distances(graph, coloring, 0)
        black_distances = get_distances(graph, coloring, 1)
        
        # Get the maximum distance between white and black vertices
        max_white_distance = max(white_distances) if white_distances else 0
        max_black_distance = max(black_distances) if black_distances else 0
        
        # Add the niceness of this coloring to the total niceness
        niceness += max(max_white_distance, max_black_distance)
    
    # Return the total niceness modulo 10^9 + 7
    return niceness % (10**9 + 7)

def get_distances(graph, coloring, color):
    # Initialize the distances as an empty list
    distances = []
    
    # Iterate over all vertices in the graph
    for vertex in graph:
        # If the vertex is colored with the given color, add its distance to the list of distances
        if coloring[vertex - 1] == color:
            distances.append(graph[vertex - 1])
    
    # Return the list of distances
    return distances

def main():
    # Read the number of vertices and edges from stdin
    num_vertices, num_edges = map(int, input().split())
    
    # Initialize the graph as an empty dictionary
    graph = {}
    
    # Read the edges from stdin and add them to the graph
    for _ in range(num_edges):
        edge = list(map(int, input().split()))
        graph[edge[0]] = edge[1]
        graph[edge[1]] = edge[0]
    
    # Call the get_niceness function and print the result
    print(get_niceness(graph))

if __name__ == '__main__':
    main()

