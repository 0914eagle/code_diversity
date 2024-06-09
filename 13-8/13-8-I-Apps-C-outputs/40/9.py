
def generate_main_office(N):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Generate the first vertex
    x = 0
    y = 0
    vertices.append((x, y))
    
    # Generate the remaining vertices
    for i in range(1, N):
        # Generate a random integer between 0 and 40000000
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Ensure that the vertex is not collinear with any of the existing vertices
        while not is_convex_polygon(vertices + [(x, y)]):
            x = random.randint(0, 40000000)
            y = random.randint(0, 40000000)
        
        # Add the vertex to the list of vertices
        vertices.append((x, y))
    
    return vertices

def is_convex_polygon(vertices):
    # Check if the polygon is convex
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i == j:
                continue
            for k in range(len(vertices)):
                if i == k or j == k:
                    continue
                if not is_collinear(vertices[i], vertices[j], vertices[k]):
                    return False
    
    return True

def is_collinear(p1, p2, p3):
    # Check if the three points are collinear
    if p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1]) == 0:
        return True
    else:
        return False

