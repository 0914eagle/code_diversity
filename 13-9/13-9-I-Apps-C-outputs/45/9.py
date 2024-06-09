
def get_convex_polygon(n):
    result = []
    for i in range(n):
        result.append((i, 0))
    for i in range(n):
        result.append((40000000, i))
    for i in range(n):
        result.append((40000000 - i, 40000000))
    return result

