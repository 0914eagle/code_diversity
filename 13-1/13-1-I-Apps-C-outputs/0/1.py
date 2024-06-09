
def get_cube_vertices(lines):
    vertices = []
    for line in lines:
        vertices.append([int(x) for x in line.split()])
    return vertices

def is_cube(vertices):
    if len(vertices) != 8:
        return False
    for i in range(3):
        for j in range(i+1, 3):
            for k in range(j+1, 3):
                if not is_permutation(vertices[i], vertices[j], vertices[k]):
                    return False
    return True

def is_permutation(a, b, c):
    return sorted(a) == sorted(b) and sorted(b) == sorted(c)

def restore_cube(lines):
    vertices = get_cube_vertices(lines)
    if is_cube(vertices):
        return "YES\n" + "\n".join([" ".join(map(str, vertex)) for vertex in vertices])
    else:
        return "NO"

if __name__ == '__main__':
    lines = [input() for _ in range(8)]
    print(restore_cube(lines))

