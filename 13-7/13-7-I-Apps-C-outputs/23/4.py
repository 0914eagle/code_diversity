
def get_hexagon_circumference(vertices):
    
    # Sort the vertices by their x-coordinates
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Initialize the maximum circumference and the indices of the vertices to be used
    max_circumference = 0
    vertex_indices = []

    # Iterate over all possible combinations of 6 vertices
    for i in range(len(sorted_vertices) - 5):
        for j in range(i + 1, len(sorted_vertices) - 4):
            for k in range(j + 1, len(sorted_vertices) - 3):
                for l in range(k + 1, len(sorted_vertices) - 2):
                    for m in range(l + 1, len(sorted_vertices) - 1):
                        for n in range(m + 1, len(sorted_vertices)):
                            # Calculate the circumference of the hexagon
                            circumference = get_hexagon_circumference_helper(sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n])

                            # Update the maximum circumference and the indices of the vertices if necessary
                            if circumference > max_circumference:
                                max_circumference = circumference
                                vertex_indices = [i, j, k, l, m, n]

    return max_circumference

def get_hexagon_circumference_helper(v1, v2, v3, v4, v5, v6):
    
    return get_distance(v1, v2) + get_distance(v2, v3) + get_distance(v3, v4) + get_distance(v4, v5) + get_distance(v5, v6) + get_distance(v6, v1)

def get_distance(v1, v2):
    
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5

