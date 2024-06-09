
def generate_main_office(n):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to n-1
    for i in range(n):
        # Generate a random x and y coordinate for the current vertex
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Check if the current vertex is already in the list of vertices
        if [x, y] in vertices:
            # If it is, generate a new coordinate until we find one that is not in the list
            while [x, y] in vertices:
                x = random.randint(0, 40000000)
                y = random.randint(0, 40000000)
        
        # Add the current vertex to the list of vertices
        vertices.append([x, y])
    
    # Return the list of vertices
    return vertices

