
def generate_main_office(N):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to N-1
    for i in range(N):
        # Generate a random x and y coordinate for the current vertex
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Check if the current vertex is already in the list of vertices
        if [x, y] not in vertices:
            # If not, add it to the list of vertices
            vertices.append([x, y])
    
    # Return the list of vertices
    return vertices

