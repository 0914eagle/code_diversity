
def get_maximum_circumference(n, vertices):
    # Sort the vertices by their x-coordinates
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference and the corresponding vertex indices
    max_circumference = 0
    vertex_indices = []

    # Iterate over the sorted vertices
    for i in range(n):
        # Get the current vertex and its x-coordinate
        vertex = sorted_vertices[i]
        x = vertex[0]

        # Find the next vertex with a different x-coordinate
        for j in range(i+1, n):
            next_vertex = sorted_vertices[j]
            if next_vertex[0] != x:
                break

        # Calculate the circumference of the hexagon with the current vertex as a center
        circumference = get_hexagon_circumference(vertex, sorted_vertices[i-1], vertex, next_vertex, sorted_vertices[j+1], next_vertex)

        # Update the maximum circumference and the corresponding vertex indices
        if circumference > max_circumference:
            max_circumference = circumference
            vertex_indices = [i, i-1, i, j, j+1, j]

    return max_circumference, vertex_indices

def get_hexagon_circumference(v1, v2, v3, v4, v5, v6):
    # Calculate the side lengths of the hexagon
    a = get_distance(v1, v2)
    b = get_distance(v2, v3)
    c = get_distance(v3, v4)
    d = get_distance(v4, v5)
    e = get_distance(v5, v6)
    f = get_distance(v6, v1)

    # Calculate the circumference of the hexagon
    circumference = a + b + c + d + e + f

    return circumference

def get_distance(v1, v2):
    # Calculate the Euclidean distance between two vertices
    return ((v1[0]-v2[0])**2 + (v1[1]-v2[1])**2)**0.5

