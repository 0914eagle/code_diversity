
def get_color_combinations(tile_colors):
    
    combinations = []
    for i in range(len(tile_colors)):
        for j in range(i+1, len(tile_colors)):
            for k in range(j+1, len(tile_colors)):
                combinations.append([tile_colors[i], tile_colors[j], tile_colors[k]])
    return combinations

def get_tile_colors(tile_colors, tile_number):
    
    return tile_colors[tile_number-1]

def get_cube_colors(tile_colors, cube_configuration):
    
    cube_colors = []
    for tile_number in cube_configuration:
        tile_colors = get_tile_colors(tile_colors, tile_number)
        cube_colors.extend(tile_colors)
    return cube_colors

def get_unique_cubes(tile_colors):
    
    unique_cubes = set()
    for tile_combination in itertools.combinations(range(1, len(tile_colors)+1), 6):
        cube_configuration = list(itertools.permutations(tile_combination, 6))
        for configuration in cube_configuration:
            cube_colors = get_cube_colors(tile_colors, configuration)
            unique_cubes.add(tuple(cube_colors))
    return len(unique_cubes)

def main():
    tile_colors = []
    for _ in range(int(input())):
        tile_colors.append(list(map(int, input().split())))
    print(get_unique_cubes(tile_colors))

if __name__ == '__main__':
    main()

