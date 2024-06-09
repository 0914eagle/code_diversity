
def get_cube_colors(tile_colors):
    # Function to get the colors of the cube from the tile colors
    cube_colors = []
    for i in range(6):
        cube_colors.append([tile_colors[i][0], tile_colors[i][1], tile_colors[i][2]])
    return cube_colors

def get_unique_cubes(cube_colors):
    # Function to get the number of unique cubes
    unique_cubes = set()
    for i in range(len(cube_colors)):
        for j in range(i+1, len(cube_colors)):
            if cube_colors[i] == cube_colors[j]:
                unique_cubes.add(cube_colors[i])
    return len(unique_cubes)

def main():
    # Main function to read the input and print the output
    N = int(input())
    tile_colors = []
    for i in range(N):
        tile_colors.append(list(map(int, input().split())))
    cube_colors = get_cube_colors(tile_colors)
    unique_cubes = get_unique_cubes(cube_colors)
    print(unique_cubes)

if __name__ == '__main__':
    main()

