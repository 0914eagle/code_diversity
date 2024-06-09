
def get_controlled_vertices(n, a, edges):
    # Initialize a dictionary to store the controlled vertices for each vertex
    controlled_vertices = {i: 0 for i in range(1, n + 1)}
    
    # Iterate over the edges
    for edge in edges:
        # Get the parent and child vertices
        parent, child = edge
        
        # If the child vertex is in the subtree of the parent vertex and the distance between them is less than or equal to the value written in the parent vertex
        if child in controlled_vertices and controlled_vertices[parent] + 1 <= a[parent]:
            # Increment the controlled vertices count for the parent vertex
            controlled_vertices[parent] += 1
    
    return controlled_vertices

def main():
    # Read the input
    n = int(input())
    a = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
    
    # Get the controlled vertices for each vertex
    controlled_vertices = get_controlled_vertices(n, a, edges)
    
    # Print the result
    print(*controlled_vertices.values(), sep='\n')

if __name__ == '__main__':
    main()

