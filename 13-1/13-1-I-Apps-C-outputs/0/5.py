
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
                if not is_collinear(vertices[i], vertices[j], vertices[k]):
                    return False
    return True

def is_collinear(a, b, c):
    return (b[1]-a[1])*(c[2]-a[2]) == (b[2]-a[2])*(c[1]-a[1])

def get_cube_edges(vertices):
    edges = []
    for i in range(3):
        for j in range(i+1, 3):
            edges.append((vertices[i], vertices[j]))
    return edges

def get_cube_faces(edges):
    faces = []
    for edge in edges:
        faces.append([edge[0], edge[1]])
    return faces

def get_cube_center(vertices):
    x = sum(v[0] for v in vertices) / 8
    y = sum(v[1] for v in vertices) / 8
    z = sum(v[2] for v in vertices) / 8
    return [x, y, z]

def get_cube_length(vertices):
    x1, y1, z1 = vertices[0]
    x2, y2, z2 = vertices[1]
    return max(abs(x1-x2), abs(y1-y2), abs(z1-z2))

def get_cube_volume(vertices):
    x1, y1, z1 = vertices[0]
    x2, y2, z2 = vertices[1]
    x3, y3, z3 = vertices[2]
    x4, y4, z4 = vertices[3]
    x5, y5, z5 = vertices[4]
    x6, y6, z6 = vertices[5]
    x7, y7, z7 = vertices[6]
    x8, y8, z8 = vertices[7]
    return abs((x1-x2)*(y3-y4)*(z5-z6) + (x3-x4)*(y1-y2)*(z5-z6) + (x5-x6)*(y1-y2)*(z3-z4) - (x1-x2)*(y3-y4)*(z7-z8) - (x3-x4)*(y1-y2)*(z7-z8) - (x5-x6)*(y1-y2)*(z7-z8))

def is_valid_cube(vertices):
    edges = get_cube_edges(vertices)
    faces = get_cube_faces(edges)
    center = get_cube_center(vertices)
    length = get_cube_length(vertices)
    volume = get_cube_volume(vertices)
    return is_cube(vertices) and length > 0 and volume > 0 and all(is_collinear(center, v, faces[i][0]) for i in range(6)) and all(is_collinear(center, v, faces[i][1]) for i in range(6))

def restore_cube(lines):
    vertices = get_cube_vertices(lines)
    if is_valid_cube(vertices):
        return "YES\n" + "\n".join(" ".join(str(x) for x in v) for v in vertices)
    else:
        return "NO"

if __name__ == '__main__':
    lines = [input() for _ in range(8)]
    print(restore_cube(lines))

