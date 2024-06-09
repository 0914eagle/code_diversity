
def solve(N):
    # Initialize a list to store the vertices of the polygon
    vertices = []

    # Iterate from 0 to N-1
    for i in range(N):
        # Generate a random integer between 0 and 40000000 (inclusive)
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)

        # Check if the vertex is already present in the list
        if [x, y] in vertices:
            # If the vertex is already present, generate a new one
            continue

        # Add the vertex to the list
        vertices.append([x, y])

    # Return the list of vertices
    return vertices

