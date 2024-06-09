
def solve(n, polyhedrons):
    faces = 0
    for polyhedron in polyhedrons:
        if polyhedron == "Tetrahedron":
            faces += 4
        elif polyhedron == "Cube":
            faces += 6
        elif polyhedron == "Octahedron":
            faces += 8
        elif polyhedron == "Dodecahedron":
            faces += 12
        else:
            faces += 20
    return faces
