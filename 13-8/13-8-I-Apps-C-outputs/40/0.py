
def solve(N):
    # Initialize an empty list to store the vertices of the polygon
    vertices = []
    
    # Iterate from 0 to N-1
    for i in range(N):
        # Generate a random x and y coordinate for the current vertex
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Check if the current vertex is already present in the list of vertices
        if [x, y] in vertices:
            # If the vertex is already present, generate a new coordinate
            continue
        
        # Add the current vertex to the list of vertices
        vertices.append([x, y])
    
    # Return the list of vertices
    return vertices

