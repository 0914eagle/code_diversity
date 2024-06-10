
def read_grid():
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))
    return grid

def check_grid(grid):
    a_set = set()
    b_set = set()
    for i in range(3):
        for j in range(3):
            a_set.add(grid[i][j] - grid[i][0])
            b_set.add(grid[0][j] - grid[i][j])
    if len(a_set) == 3 and len(b_set) == 3:
        return True
    else:
        return False

def main():
    grid = read_grid()
    print("Yes") if check_grid(grid) else print("No")

if __name__ == '__main__':
    main()

