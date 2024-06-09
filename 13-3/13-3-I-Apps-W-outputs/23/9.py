
def solve(n, a):
    # Initialize a list to store the vertices
    vertices = []
    
    # Iterate from 1 to n
    for i in range(1, n+1):
        # Calculate the angle between the current vertex and the next vertex
        angle = (i * 360) / n
        
        # If the angle is within the given angle a, add it to the list of vertices
        if angle <= a:
            vertices.append(i)
    
    # If the list of vertices is empty, return -1
    if not vertices:
        return -1
    
    # If the list of vertices has only one element, return that element
    if len(vertices) == 1:
        return vertices[0]
    
    # If the list of vertices has two elements, return the smallest element
    if len(vertices) == 2:
        return min(vertices)
    
    # If the list of vertices has three elements, return the smallest element
    if len(vertices) == 3:
        return min(vertices)
    
    # If the list of vertices has four elements, return the smallest element
    if len(vertices) == 4:
        return min(vertices)
    
    # If the list of vertices has more than four elements, find the smallest element that is greater than the smallest element
    smallest = min(vertices)
    for i in range(smallest+1, smallest+len(vertices)):
        if i in vertices:
            return i
    
    # If no such element is found, return -1
    return -1

