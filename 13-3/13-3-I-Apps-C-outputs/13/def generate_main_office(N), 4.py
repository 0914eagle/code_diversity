
def generate_main_office(N):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to N-1
    for i in range(N):
        # Generate a random integer between 0 and 40000000 (inclusive)
        x = random.randint(0, 40000000)
        # Generate a random integer between 0 and 40000000 (inclusive)
        y = random.randint(0, 40000000)
        # Add the vertex to the list of vertices
        vertices.append((x, y))
    
    # Return the list of vertices
    return vertices

