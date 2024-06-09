
def solve(n, a):
    # Initialize a list to store the vertices
    vertices = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Calculate the angle between the current vertex and the next vertex
        angle = (i * 360) / n

        # If the angle is close enough to the needed angle, add it to the list of vertices
        if abs(angle - a) <= 1:
            vertices.append(i)

    # If there are three vertices, return them
    if len(vertices) == 3:
        return " ".join(map(str, vertices))

    # If there are two vertices, return any of them
    if len(vertices) == 2:
        return " ".join(map(str, vertices))

    # If there is only one vertex, return it
    if len(vertices) == 1:
        return str(vertices[0])

    # If there are no vertices, return -1
    return -1

