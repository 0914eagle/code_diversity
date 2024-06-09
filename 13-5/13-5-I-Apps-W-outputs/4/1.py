
def get_max_score(graph):
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over the edges in the graph
    for edge in graph:
        # If the edge leads to a vertex with a higher score, update the maximum score
        if edge[2] > max_score:
            max_score = edge[2]
    
    # Return the maximum score
    return max_score

def main():
    # Read the number of vertices and edges from stdin
    num_vertices, num_edges = map(int, input().split())
    
    # Read the edges from stdin
    edges = []
    for _ in range(num_edges):
        edges.append(list(map(int, input().split())))
    
    # Create a graph from the edges
    graph = [[] for _ in range(num_vertices + 1)]
    for edge in edges:
        graph[edge[0]].append((edge[1], edge[2]))
    
    # Find the maximum score in the graph
    max_score = get_max_score(graph)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

