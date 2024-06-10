
def get_cube_tiles(N):
    # Function to get the tiles for the cube
    tiles = []
    for i in range(N):
        tiles.append([])
        for j in range(4):
            tiles[i].append(int(input()))
    return tiles

def get_cube_colors(tiles):
    # Function to get the colors of the cube
    colors = []
    for i in range(4):
        colors.append([])
        for j in range(4):
            colors[i].append(tiles[i][j])
    return colors

def get_cube_neighbors(cube):
    # Function to get the neighbors of a cube
    neighbors = []
    for i in range(4):
        neighbors.append([])
        for j in range(4):
            neighbors[i].append(cube[j][(i+1)%4])
    return neighbors

def get_cube_rotations(cube):
    # Function to get the rotations of a cube
    rotations = []
    for i in range(4):
        rotations.append([])
        for j in range(4):
            rotations[i].append(cube[j][(i+1)%4])
    return rotations

def get_cube_directions(cube):
    # Function to get the directions of a cube
    directions = []
    for i in range(4):
        directions.append([])
        for j in range(4):
            directions[i].append(cube[j][(i+1)%4])
    return directions

def get_unique_cubes(N):
    # Function to get the unique cubes
    unique_cubes = set()
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if i != j and i != k and i != l and j != k and j != l and k != l:
                        cube = [[i, j, k, l], [i, l, k, j], [j, l, i, k], [j, k, l, i], [k, l, j, i], [k, i, j, l]]
                        unique_cubes.add(frozenset(cube))
    return len(unique_cubes)

def main():
    N = int(input())
    tiles = get_cube_tiles(N)
    colors = get_cube_colors(tiles)
    neighbors = get_cube_neighbors(colors)
    rotations = get_cube_rotations(colors)
    directions = get_cube_directions(colors)
    unique_cubes = get_unique_cubes(N)
    print(unique_cubes)

if __name__ == '__main__':
    main()

