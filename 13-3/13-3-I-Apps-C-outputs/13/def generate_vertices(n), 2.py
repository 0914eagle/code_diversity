
def generate_vertices(n):
    vertices = []
    for i in range(n):
        vertices.append((i, 0))
    for i in range(n):
        vertices.append((40000000, i))
    for i in range(n):
        vertices.append((i, 40000000))
    return vertices

