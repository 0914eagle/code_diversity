
def generate_vertices(n):
    # Initialize a list to store the vertices
    vertices = []
    
    # Iterate from 0 to n-1
    for i in range(n):
        # Generate a random integer between 0 and 40000000 (inclusive)
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Check if the vertex is already present in the list
        if [x, y] in vertices:
            # If present, generate a new vertex
            continue
        else:
            # If not present, add it to the list
            vertices.append([x, y])
    
    # Return the list of vertices
    return vertices

