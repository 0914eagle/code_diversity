
def canyon_mapping(n, k, vertices):
    # Sort the vertices based on their x-coordinate
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Calculate the width of the canyon
    width = sorted_vertices[-1][0] - sorted_vertices[0][0]

    # Calculate the height of the canyon
    height = sorted_vertices[-1][1] - sorted_vertices[0][1]

    # Calculate the side length of the square maps
    side_length = width / k

    return round(side_length, 2)

