
def get_score(graph, start, end):
    
    # Base case: if we are already at the end vertex, return the score
    if start == end:
        return 0
    
    # Initialize the maximum score to 0
    max_score = 0
    
    # Iterate over the edges incident to the start vertex
    for edge in graph[start]:
        # Get the end vertex and score of the edge
        end_vertex, score = edge
        
        # Recursively call the function to move the piece to the end vertex and add the score
        max_score = max(max_score, score + get_score(graph, end_vertex, end))
    
    # Return the maximum score
    return max_score

def main():
    # Read the input from stdin
    num_vertices, num_edges = map(int, input().split())
    graph = [[] for _ in range(num_vertices + 1)]
    for _ in range(num_edges):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    
    # Call the function to get the maximum score and print the result
    print(get_score(graph, 1, num_vertices))

if __name__ == '__main__':
    main()

