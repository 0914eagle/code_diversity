
def f1(N, C):
    # Initialize a dictionary to store the number of cubes for each color
    num_cubes = {}
    for i in range(N):
        for j in range(4):
            # Get the color of the current corner
            color = C[i][j]
            # If the color is not in the dictionary, add it with a count of 1
            if color not in num_cubes:
                num_cubes[color] = 1
            # If the color is already in the dictionary, increment its count
            else:
                num_cubes[color] += 1
    # Return the number of cubes
    return len(num_cubes)

def f2(N, C):
    # Initialize a set to store the colors of the cubes
    cube_colors = set()
    for i in range(N):
        for j in range(4):
            # Get the color of the current corner
            color = C[i][j]
            # Add the color to the set
            cube_colors.add(color)
    # Return the number of cubes
    return len(cube_colors)

if __name__ == '__main__':
    N = int(input())
    C = []
    for i in range(N):
        C.append(list(map(int, input().split())))
    print(f2(N, C))

