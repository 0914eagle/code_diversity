
def get_cube_data():
    N = int(input())
    cube = []
    for i in range(N):
        cube.append(list(map(int, input().split())))
    return cube

def get_cube_colors(cube):
    colors = set()
    for tile in cube:
        for color in tile:
            colors.add(color)
    return colors

def get_cube_rotations(cube):
    rotations = []
    for i in range(4):
        rotated_cube = []
        for tile in cube:
            rotated_tile = []
            for j in range(4):
                rotated_tile.append(tile[(j+i)%4])
            rotated_cube.append(rotated_tile)
        rotations.append(rotated_cube)
    return rotations

def get_cube_combinations(cube):
    combinations = []
    for i in range(4):
        for j in range(i+1, 4):
            combinations.append((cube[i], cube[j]))
    return combinations

def get_cube_count(cube):
    colors = get_cube_colors(cube)
    rotations = get_cube_rotations(cube)
    combinations = get_cube_combinations(cube)
    count = 0
    for color in colors:
        for rotation in rotations:
            for combination in combinations:
                if all(color in tile for tile in combination):
                    count += 1
    return count

def main():
    cube = get_cube_data()
    print(get_cube_count(cube))

if __name__ == '__main__':
    main()

