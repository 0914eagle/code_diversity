
def generate_main_office(n):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to n-1
    for i in range(n):
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

def is_collinear(p1, p2):
    # Calculate the slope between the two points
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    # Check if the slope is equal to the slope between any two other points
    for i in range(len(vertices)):
        for j in range(i+1, len(vertices)):
            if slope == (vertices[j][1] - vertices[i][1]) / (vertices[j][0] - vertices[i][0]):
                return True
    
    # If no other points have the same slope, the points are not collinear
    return False

