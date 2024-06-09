
def get_original_coordinates(cube_vertices):
    
    # Sort the vertices
    sorted_vertices = sorted(cube_vertices)

    # Check if the vertices form a cube
    if len(set(sorted_vertices)) != 8:
        return "NO"

    # Restore the original coordinates
    original_coordinates = []
    for vertex in sorted_vertices:
        original_coordinates.append(vertex)

    return "YES\n" + "\n".join(map(str, original_coordinates))

def main():
    cube_vertices = []
    for _ in range(8):
        cube_vertices.append(list(map(int, input().split())))

    print(get_original_coordinates(cube_vertices))

if __name__ == '__main__':
    main()

