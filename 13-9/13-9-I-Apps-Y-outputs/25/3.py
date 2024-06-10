
def input_grid():
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))
    return grid

def check_takahashi(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != grid[i][0] + grid[0][j]:
                return False
    return True

def main():
    grid = input_grid()
    if check_takahashi(grid):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

