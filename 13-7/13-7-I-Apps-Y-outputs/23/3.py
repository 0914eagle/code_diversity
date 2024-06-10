
def get_input():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    move = int(input())
    return grid, move

def move_left(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == 0:
                grid[i][j] = grid[i][j+1]
                grid[i][j+1] = 0
    return grid

def move_up(grid):
    for i in range(3):
        for j in range(4):
            if grid[i][j] == 0:
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = 0
    return grid

def move_right(grid):
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] == 0:
                grid[i][j] = grid[i][j-1]
                grid[i][j-1] = 0
    return grid

def move_down(grid):
    for i in range(3, -1, -1):
        for j in range(4):
            if grid[i][j] == 0:
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = 0
    return grid

def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    for i in range(4):
        for j in range(3):
            if grid[j][i] == grid[j+1][i]:
                grid[j][i] *= 2
                grid[j+1][i] = 0
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
    for i in range(4):
        print(*grid[i])

if __name__ == '__main__':
    main()

