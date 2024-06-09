
def get_original_coordinates(cube_vertices):
    # Sort the vertices
    sorted_vertices = sorted(cube_vertices)

    # Check if the vertices form a cube
    if len(set(sorted_vertices)) == 8:
        return sorted_vertices
    else:
        return None

def main():
    cube_vertices = []
    for _ in range(8):
        cube_vertices.append(list(map(int, input().split())))

    original_coordinates = get_original_coordinates(cube_vertices)
    if original_coordinates:
        print("YES")
        for coordinate in original_coordinates:
            print(*coordinate)
    else:
        print("NO")

if __name__ == '__main__':
    main()

