
def solve(n, a):
    # Initialize a list to store the vertices
    vertices = []

    # Iterate from 1 to n
    for i in range(1, n + 1):
        # Calculate the angle between the current vertex and the previous vertex
        if i == 1:
            angle = 360 - a
        else:
            angle = (360 / n) - a

        # If the angle is less than or equal to a, add the current vertex to the list
        if angle <= a:
            vertices.append(i)

    # If the list has three elements, return the vertices
    if len(vertices) == 3:
        return " ".join(map(str, vertices))

    # If the list has two elements, return the vertices in reverse order
    if len(vertices) == 2:
        return " ".join(map(str, vertices[::-1]))

    # If the list has one element, return the vertex and the next vertex
    if len(vertices) == 1:
        return " ".join(map(str, [vertices[0], vertices[0] + 1]))

    # If the list is empty, return -1
    return -1

