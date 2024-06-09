
def solve(n, a):
    # Initialize a list to store the vertices
    vertices = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Calculate the angle between the current vertex and the next vertex
        angle = (360 - a) / 2

        # If the angle is less than 180 degrees, add the current vertex to the list
        if angle < 180:
            vertices.append(i)

    # If the list has three elements, return the vertices
    if len(vertices) == 3:
        return vertices

    # If the list has two elements, return the vertices in a specific order
    if len(vertices) == 2:
        return [vertices[0], vertices[1] + 1, vertices[0] + 1]

    # If the list has one element, return the vertices in a specific order
    if len(vertices) == 1:
        return [vertices[0], vertices[0] + 1, vertices[0] + 2]

    # If the list is empty, return an error message
    return "Error: Invalid input"

