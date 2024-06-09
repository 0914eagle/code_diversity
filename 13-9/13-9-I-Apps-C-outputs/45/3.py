
def generate_vertices(n):
    for i in range(n):
        x = random.randint(0, 40000000)
        y = random.randint(0, 40000000)
        yield (x, y)

