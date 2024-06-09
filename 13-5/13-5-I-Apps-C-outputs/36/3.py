
def get_cube_colors(tile_colors):
    # Convert the tile colors to a set of tuples representing the corner colors
    cube_colors = set()
    for i in range(len(tile_colors)):
        for j in range(4):
            cube_colors.add(tuple(tile_colors[i][j]))
    return cube_colors

def get_cube_rotations(cube_colors):
    # Get all possible rotations of the cube
    cube_rotations = set()
    for i in range(len(cube_colors)):
        for j in range(4):
            cube_rotations.add(tuple(cube_colors[i][j]))
    return cube_rotations

def get_unique_cubes(cube_rotations):
    # Get the number of unique cubes
    unique_cubes = len(cube_rotations)
    return unique_cubes

def main():
    # Read the input
    N = int(input())
    tile_colors = []
    for i in range(N):
        tile_colors.append(list(map(int, input().split())))

    # Get the cube colors and rotations
    cube_colors = get_cube_colors(tile_colors)
    cube_rotations = get_cube_rotations(cube_colors)

    # Get the number of unique cubes
    unique_cubes = get_unique_cubes(cube_rotations)

    # Print the result
    print(unique_cubes)

if __name__ == '__main__':
    main()

