
def get_vertices(n):
    vertices = []
    for i in range(n):
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        vertices.append((x, y))
    return vertices

