
def get_main_office_vertices(N):
    vertices = []
    for i in range(N):
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        vertices.append((x, y))
    return vertices

