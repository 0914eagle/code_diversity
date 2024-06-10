
def get_input():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    move = int(input())
    return grid, move

def move_left(grid):
    for i in range(4):
        grid[i] = [grid[i][j] for j in range(4) if grid[i][j] != 0] + [0] * (4 - len(grid[i]))
    return grid

def move_up(grid):
    return [list(row) for row in zip(*grid[::-1])]

def move_right(grid):
    for i in range(4):
        grid[i] = grid[i][::-1]
    return grid

def move_down(grid):
    for i in range(4):
        grid[i] = grid[i][::-1]
    return [list(row) for row in zip(*grid[::-1])]

def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    return grid

def solve(grid, move):
    if move == 0:
        return move_left(grid)
    elif move == 1:
        return move_up(grid)
    elif move == 2:
        return move_right(grid)
    else:
        return move_down(grid)

def main():
    grid, move = get_input()
    grid = solve(grid, move)
    grid = merge(grid)
    for row in grid:
        print(*row)

if __name__ == '__main__':
    main()

