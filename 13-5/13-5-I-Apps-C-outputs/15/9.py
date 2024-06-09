
def get_controlled_vertices(n, a, edges):
    # Initialize a dictionary to store the controlled vertices for each vertex
    controlled_vertices = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges
    for edge in edges:
        # Get the parent and child vertices
        parent, child = edge
        
        # If the child vertex is in the subtree of the parent vertex and the distance between them is less than or equal to a_child, then the parent vertex controls the child vertex
        if child in range(parent * 2, parent * 2 + n) and sum(edges[parent]) <= a[child]:
            controlled_vertices[parent] += 1
    
    return controlled_vertices

def main():
    # Read the input data
    n = int(input())
    a = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    # Get the controlled vertices for each vertex
    controlled_vertices = get_controlled_vertices(n, a, edges)
    
    # Print the number of controlled vertices for each vertex
    for vertex in controlled_vertices:
        print(controlled_vertices[vertex])

if __name__ == '__main__':
    main()

