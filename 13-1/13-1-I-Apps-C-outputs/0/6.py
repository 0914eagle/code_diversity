
def get_cube_vertices(vertices):
    # Sort the vertices
    sorted_vertices = sorted(vertices)

    # Check if the vertices form a cube
    if len(set(sorted_vertices)) == 8:
        return sorted_vertices
    else:
        return None

def restore_cube_vertices(vertices):
    # Get the cube vertices
    cube_vertices = get_cube_vertices(vertices)

    # If the vertices form a cube, return them
    if cube_vertices:
        return cube_vertices

    # If the vertices do not form a cube, return None
    return None

if __name__ == '__main__':
    vertices = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
    restored_vertices = restore_cube_vertices(vertices)
    if restored_vertices:
        print("YES")
        for vertex in restored_vertices:
            print(" ".join(map(str, vertex)))
    else:
        print("NO")

