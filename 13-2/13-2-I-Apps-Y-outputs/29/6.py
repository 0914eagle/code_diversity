
def move_left(grid):
    
    for i in range(4):
        grid[i] = [grid[i][j] for j in range(4) if grid[i][j] != 0]
        grid[i] = [0] * (4 - len(grid[i])) + grid[i]
    return grid

def move_right(grid):
    
    for i in range(4):
        grid[i] = grid[i][::-1]
    grid = move_left(grid)
    for i in range(4):
        grid[i] = grid[i][::-1]
    return grid

def move_up(grid):
    
    return move_left(grid)

def move_down(grid):
    
    return move_left(grid[::-1])[::-1]

def merge(grid):
    
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0
    return grid

def get_next_state(grid, move):
    
    if move == 0:
        return move_left(grid)
    elif move == 1:
        return move_up(grid)
    elif move == 2:
        return move_right(grid)
    else:
        return move_down(grid)

def get_final_state(grid, move):
    
    grid = get_next_state(grid, move)
    grid = merge(grid)
    return grid

def main():
    grid = [[int(x) for x in input().split()] for _ in range(4)]
    move = int(input())
    grid = get_final_state(grid, move)
    for row in grid:
        print(*row)

if __name__ == '__main__':
    main()

