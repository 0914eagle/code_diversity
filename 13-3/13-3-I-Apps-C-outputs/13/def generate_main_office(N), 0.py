
def generate_main_office(N):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to N-1
    for i in range(N):
        # Generate a random x and y coordinate for the current vertex
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Check if the current vertex is not collinear with any of the previous vertices
        collinear = False
        for j in range(len(vertices)):
            if is_collinear(vertices[j], (x, y)):
                collinear = True
                break
        
        # If the current vertex is not collinear, add it to the list of vertices
        if not collinear:
            vertices.append((x, y))
    
    # Return the list of vertices
    return vertices

# Function to check if three points are collinear
def is_collinear(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return x1*y2 == x2*y1

