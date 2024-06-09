
def count_triangles(A, B, C, D):
    count = 0
    for x in range(A, B+1):
        for y in range(x, B+1):
            for z in range(y, C+1):
                if x + y > z and x + z > y and y + z > x:
                    count += 1
    return count

