
def solve(n, polyhedrons):
    faces = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }
    total_faces = 0
    for polyhedron in polyhedrons:
        total_faces += faces[polyhedron]
    return total_faces

