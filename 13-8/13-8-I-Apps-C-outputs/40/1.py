
def main_office_vertices(N):
    # Initialize a list to store the vertices of the main office
    vertices = []
    
    # Iterate from 0 to N-1
    for i in range(N):
        # Calculate the x and y coordinates of the current vertex
        x = i * (40000000 // N)
        y = (i * (40000000 // N)) ** 2
        
        # Add the current vertex to the list of vertices
        vertices.append((x, y))
    
    # Return the list of vertices
    return vertices

