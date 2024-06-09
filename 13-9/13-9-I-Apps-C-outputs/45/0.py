
import sys

def get_vertices(N):
    # Validate input
    if N < 3 or N > 400000:
        raise ValueError("Invalid input")
    
    # Initialize variables
    vertices = []
    x = 0
    y = 0
    
    # Generate vertices
    for i in range(N):
        # Generate random x and y coordinates
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Ensure that the coordinates are distinct and form a convex polygon
        while (x, y) in vertices or not is_convex_polygon(vertices + [(x, y)]):
            x = random.randint(0, 40000000)
            y = random.randint(0, 40000000)
        
        # Add vertex to list
        vertices.append((x, y))
    
    return vertices

def is_convex_polygon(vertices):
    # Validate input
    if len(vertices) < 3:
        return False
    
    # Initialize variables
    prev = vertices[0]
    curr = vertices[1]
    next = vertices[2]
    convex = True
    
    # Check if the polygon is convex
    for i in range(len(vertices)):
        # Check if the current vertex is collinear with the previous two vertices
        if is_collinear(prev, curr, next):
            convex = False
            break
        
        # Update vertices
        prev = curr
        curr = next
        next = vertices[(i + 1) % len(vertices)]
    
    return convex

def is_collinear(a, b, c):
    # Calculate the slope of the line between a and b
    slope = (b[1] - a[1]) / (b[0] - a[0])
    
    # Calculate the y-intercept of the line
    y_intercept = a[1] - slope * a[0]
    
    # Check if the point c lies on the line
    return abs(slope * c[0] + y_intercept - c[1]) <= 1e-9

if __name__ == "__main__":
    N = int(input())
    vertices = get_vertices(N)
    for vertex in vertices:
        print(vertex[0], vertex[1])

