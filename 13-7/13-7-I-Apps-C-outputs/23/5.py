
def get_max_circumference(vertices):
    # Sort the vertices in counterclockwise order
    sorted_vertices = sorted(vertices, key=lambda v: v[0] * v[1])

    # Initialize the maximum circumference and the vertices of the hexagon
    max_circumference = 0
    hexagon = []

    # Iterate over all possible combinations of 6 vertices
    for i in range(len(sorted_vertices)):
        for j in range(i+1, len(sorted_vertices)):
            for k in range(j+1, len(sorted_vertices)):
                for l in range(k+1, len(sorted_vertices)):
                    for m in range(l+1, len(sorted_vertices)):
                        for n in range(m+1, len(sorted_vertices)):
                            # Check if the 6 vertices form a convex hexagon
                            if is_convex_hexagon(sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n]):
                                # Calculate the circumference of the hexagon
                                circumference = get_circumference(sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n])

                                # Update the maximum circumference and the vertices of the hexagon
                                if circumference > max_circumference:
                                    max_circumference = circumference
                                    hexagon = [sorted_vertices[i], sorted_vertices[j], sorted_vertices[k], sorted_vertices[l], sorted_vertices[m], sorted_vertices[n]]

    return hexagon, max_circumference

def is_convex_hexagon(v1, v2, v3, v4, v5, v6):
    # Calculate the orientation of the hexagon
    orientation = get_orientation(v1, v2, v3, v4, v5, v6)

    # Check if the hexagon is convex
    if orientation == 0:
        return False
    else:
        return True

def get_orientation(v1, v2, v3, v4, v5, v6):
    # Calculate the orientation of the hexagon
    orientation = (v2[0] - v1[0]) * (v3[1] - v2[1]) + (v3[0] - v2[0]) * (v1[1] - v3[1])
    orientation += (v4[0] - v3[0]) * (v5[1] - v4[1]) + (v5[0] - v4[0]) * (v3[1] - v5[1])
    orientation += (v6[0] - v5[0]) * (v1[1] - v6[1]) + (v1[0] - v6[0]) * (v5[1] - v1[1])

    return orientation

def get_circumference(v1, v2, v3, v4, v5, v6):
    # Calculate the length of the sides of the hexagon
    a = get_distance(v1, v2)
    b = get_distance(v2, v3)
    c = get_distance(v3, v4)
    d = get_distance(v4, v5)
    e = get_distance(v5, v6)
    f = get_distance(v6, v1)

    # Calculate the perimeter of the hexagon
    perimeter = a + b + c + d + e + f

    return perimeter

def get_distance(v1, v2):
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** 0.5

