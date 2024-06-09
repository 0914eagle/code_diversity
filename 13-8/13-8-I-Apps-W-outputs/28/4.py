
def get_minimal_bdd_vertices(n, function):
    # Initialize a dictionary to store the BDD vertices
    vertices = {}

    # Initialize the root vertex with the function value
    root = (0, function[0])
    vertices[0] = root

    # Iterate over the remaining function values
    for i in range(1, 2**n):
        # Get the current vertex and its label
        current_vertex = vertices[i-1]
        current_label = current_vertex[1]

        # Check if the current vertex is a leaf vertex
        if current_label == function[i]:
            # If it is a leaf vertex, add it to the dictionary and continue
            vertices[i] = current_vertex
            continue

        # If the current vertex is not a leaf vertex, create two new vertices
        vertex_0 = (i*2, function[i*2])
        vertex_1 = (i*2+1, function[i*2+1])

        # Add the new vertices to the dictionary
        vertices[i*2] = vertex_0
        vertices[i*2+1] = vertex_1

        # Connect the current vertex to the new vertices
        vertices[i] = (current_vertex[0], (current_label, vertex_0, vertex_1))

    # Return the number of vertices in the minimal BDD
    return len(vertices)

