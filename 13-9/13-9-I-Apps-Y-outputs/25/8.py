
def input_grid():
    grid = []
    for _ in range(3):
        grid.append(list(map(int, input().split())))
    return grid

def check_takahashi(grid, a, b):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != a[i] + b[j]:
                return False
    return True

def main():
    grid = input_grid()
    a = [0, 1, 0]
    b = [1, 0, 1]
    if check_takahashi(grid, a, b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

