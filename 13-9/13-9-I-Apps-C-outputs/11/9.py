
def get_cube_configurations(tiles):
    configurations = set()
    for tile_1 in tiles:
        for tile_2 in tiles:
            for tile_3 in tiles:
                for tile_4 in tiles:
                    for tile_5 in tiles:
                        for tile_6 in tiles:
                            configuration = (tile_1, tile_2, tile_3, tile_4, tile_5, tile_6)
                            if is_valid_cube_configuration(configuration):
                                configurations.add(configuration)
    return configurations

def is_valid_cube_configuration(configuration):
    tile_1, tile_2, tile_3, tile_4, tile_5, tile_6 = configuration
    return (tile_1[0] == tile_2[0] and tile_1[1] == tile_3[0] and tile_1[2] == tile_4[0] and tile_1[3] == tile_5[0] and tile_1[3] == tile_6[0]) and (tile_2[1] == tile_3[1] and tile_2[2] == tile_4[1] and tile_2[3] == tile_5[1] and tile_2[3] == tile_6[1]) and (tile_3[2] == tile_4[2] and tile_3[3] == tile_5[2] and tile_3[3] == tile_6[2]) and (tile_4[3] == tile_5[3] and tile_4[3] == tile_6[3])

def get_cube_color_patterns(tiles):
    color_patterns = set()
    for tile in tiles:
        color_pattern = (tile[0], tile[1], tile[2], tile[3])
        color_patterns.add(color_pattern)
    return color_patterns

def get_cube_rotations(color_patterns):
    rotations = set()
    for color_pattern in color_patterns:
        for i in range(4):
            rotated_color_pattern = rotate_color_pattern(color_pattern, i)
            rotations.add(rotated_color_pattern)
    return rotations

def rotate_color_pattern(color_pattern, n):
    return tuple(color_pattern[i] for i in range(4))

def get_num_different_cubes(tiles):
    configurations = get_cube_configurations(tiles)
    color_patterns = get_cube_color_patterns(tiles)
    rotations = get_cube_rotations(color_patterns)
    return len(configurations) * len(rotations)

if __name__ == '__main__':
    num_tiles = int(input())
    tiles = []
    for i in range(num_tiles):
        tile = tuple(map(int, input().split()))
        tiles.append(tile)
    print(get_num_different_cubes(tiles))

