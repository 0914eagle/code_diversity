
def solve(n, vertices):
    # Sort the vertices by their x-coordinates
    sorted_vertices = sorted(vertices, key=lambda x: x[0])

    # Get the first two vertices
    v1 = sorted_vertices[0]
    v2 = sorted_vertices[1]

    # Calculate the area of the initial rectangle
    area = (v1[0] - v2[0]) * (v1[1] - v2[1])

    # If the area is negative, return -1
    if area < 0:
        return -1

    # If the area is 0, return 0
    if area == 0:
        return 0

    # If the area is positive, return the area
    return area

