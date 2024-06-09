
def convex_polygon(n):
    # Initialize a list to store the vertices of the polygon
    vertices = []
    
    # Iterate from 0 to n-1
    for i in range(n):
        # Calculate the x and y coordinates of the current vertex
        x = i * (40000000 // n)
        y = (i * (40000000 // n)) ** 2
        
        # Add the current vertex to the list of vertices
        vertices.append((x, y))
    
    # Return the list of vertices
    return vertices

