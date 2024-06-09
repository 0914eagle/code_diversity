
def generate_vertices(n):
    # Initialize a list to store the vertices
    vertices = []
    
    # Generate the first vertex
    x = 0
    y = 0
    vertices.append((x, y))
    
    # Generate the remaining vertices
    for i in range(1, n):
        # Generate a random integer between 0 and 40000000
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        
        # Ensure that the vertex is not collinear with any of the existing vertices
        while is_collinear(vertices, (x, y)):
            x = random.randint(0, 40000000)
            y = random.randint(0, 40000000)
        
        # Add the vertex to the list
        vertices.append((x, y))
    
    return vertices

def is_collinear(vertices, vertex):
    # Check if the vertex is collinear with any of the existing vertices
    for v in vertices:
        if is_on_line(v, vertex):
            return True
    return False

def is_on_line(v1, v2):
    # Check if the two vertices are on the same line
    (x1, y1) = v1
    (x2, y2) = v2
    return x1*y2 == x2*y1

def main():
    n = int(input())
    vertices = generate_vertices(n)
    for vertex in vertices:
        print(vertex[0], vertex[1])

if __name__ == "__main__":
    main()

