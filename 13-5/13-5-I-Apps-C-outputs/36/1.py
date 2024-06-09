
def f1(n, colors):
    # function to check if the colors of a cube are valid
    def is_valid_cube(cube):
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if cube[i] == cube[j] == cube[k]:
                        return False
        return True

    # function to generate all possible cubes
    def generate_cubes():
        cubes = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    cube = [i, j, k]
                    if is_valid_cube(cube):
                        cubes.append(cube)
        return cubes

    # function to count the number of valid cubes
    def count_cubes():
        cubes = generate_cubes()
        return len(cubes)

    return count_cubes()

def f2(n, colors):
    # function to check if the colors of a cube are valid
    def is_valid_cube(cube):
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if cube[i] == cube[j] == cube[k]:
                        return False
        return True

    # function to generate all possible cubes
    def generate_cubes():
        cubes = []
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    cube = [i, j, k]
                    if is_valid_cube(cube):
                        cubes.append(cube)
        return cubes

    # function to count the number of valid cubes
    def count_cubes():
        cubes = generate_cubes()
        return len(cubes)

    return count_cubes()

if __name__ == '__main__':
    n = int(input())
    colors = []
    for i in range(n):
        colors.append([int(x) for x in input().split()])
    print(f1(n, colors))

