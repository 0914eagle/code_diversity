
def get_cube_vertices(coordinates):
    # Sort the coordinates
    coordinates = sorted(coordinates)
    
    # Check if the coordinates form a cube
    if len(set(coordinates)) == 8:
        return coordinates
    else:
        return None

def main():
    coordinates = [list(map(int, input().split())) for _ in range(8)]
    restored_coordinates = get_cube_vertices(coordinates)
    if restored_coordinates:
        print("YES")
        for coordinate in restored_coordinates:
            print(" ".join(map(str, coordinate)))
    else:
        print("NO")

if __name__ == '__main__':
    main()

