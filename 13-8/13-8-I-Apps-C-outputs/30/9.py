
def find_minimum_side_length(n, k, vertices):
    
    # Sort the vertices in clockwise order
    vertices.sort(key=lambda x: (x[1], x[0]))

    # Find the bounding box of the polygon
    min_x = min(vertices, key=lambda x: x[0])[0]
    max_x = max(vertices, key=lambda x: x[0])[0]
    min_y = min(vertices, key=lambda x: x[1])[1]
    max_y = max(vertices, key=lambda x: x[1])[1]

    # Calculate the area of the polygon
    area = abs(poly_area(vertices))

    # Initialize the minimum side length to the width of the bounding box
    min_side_length = max_x - min_x

    # Iterate through each possible side length
    for side_length in range(int(min_side_length), int(max_side_length) + 1):
        # Calculate the number of maps needed to cover the polygon
        num_maps = int(ceil(area / (side_length ** 2)))

        # If the number of maps is less than or equal to k, update the minimum side length
        if num_maps <= k:
            min_side_length = side_length

    return round(min_side_length, 2)

def poly_area(vertices):
    
    area = 0
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return area / 2

