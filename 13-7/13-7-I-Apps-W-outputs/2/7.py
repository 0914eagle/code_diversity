
def count_triangles(a, b, c, d):
    count = 0
    for x in range(a, b+1):
        for y in range(x, b+1):
            for z in range(y, c+1):
                if x <= y <= z <= d:
                    count += 1
    return count

