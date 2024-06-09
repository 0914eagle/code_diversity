
def get_score(graph, start, end):
    
    if start == end:
        return 0
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over all edges connected to the start vertex
    for edge in graph[start]:
        # Get the neighbor and weight of the edge
        neighbor, weight = edge
        
        # Recursively call the function to get the maximum score from the neighbor vertex to the end vertex
        score = get_score(graph, neighbor, end)
        
        # If the score is non-negative, add the weight of the edge to the score and update the maximum score
        if score >= 0:
            max_score = max(max_score, score + weight)
    
    return max_score

def main():
    # Read the input from stdin
    num_vertices, num_edges = map(int, input().split())
    graph = {}
    for _ in range(num_edges):
        edge = tuple(map(int, input().split()))
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append((edge[1], edge[2]))
    
    # Get the maximum score from vertex 1 to vertex N
    max_score = get_score(graph, 1, num_vertices)
    
    # Print the maximum score
    print(max_score)

if __name__ == '__main__':
    main()

