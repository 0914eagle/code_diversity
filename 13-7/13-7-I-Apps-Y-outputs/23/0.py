
def input_grid():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    return grid

def move_left(grid):
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(j, -1, -1):
                    if grid[i][k] == 0:
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[i][k] == grid[i][j]:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_up(grid):
    for j in range(4):
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(i, -1, -1):
                    if grid[k][j] == 0:
                        grid[k][j] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[k][j] == grid[i][j]:
                        grid[k][j] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_right(grid):
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                for k in range(j+1, 4):
                    if grid[i][k] == 0:
                        grid[i][k] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[i][k] == grid[i][j]:
                        grid[i][k] *= 2
                        grid[i][j] = 0
                        break
    return grid

def move_down(grid):
    for j in range(4):
        for i in range(4):
            if grid[i][j] != 0:
                for k in range(i+1, 4):
                    if grid[k][j] == 0:
                        grid[k][j] = grid[i][j]
                        grid[i][j] = 0
                        break
                    elif grid[k][j] == grid[i][j]:
                        grid[k][j] *= 2
                        grid[i][j] = 0
                        break
    return grid

def main():
    grid = input_grid()
    move = int(input())
    if move == 0:
        grid = move_left(grid)
    elif move == 1:
        grid = move_up(grid)
    elif move == 2:
        grid = move_right(grid)
    else:
        grid = move_down(grid)
    for row in grid:
        print(*row)

if __name__ == '__main__':
    main()

