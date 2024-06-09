
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

def get_next_state(grid, direction):
    
    if direction == 0:
        return move_left(grid)
    elif direction == 1:
        return move_up(grid)
    elif direction == 2:
        return move_right(grid)
    else:
        return move_down(grid)

def get_score(grid):
    
    score = 0
    for i in range(4):
        for j in range(4):
            score += grid[i][j]
    return score

def f1(grid, direction):
    
    return get_next_state(grid, direction)

def f2(grid, direction):
    
    return get_score(grid)

if __name__ == '__main__':
    grid = [[2, 0, 0, 2], [4, 16, 8, 2], [2, 64, 32, 4], [1024, 1024, 64, 0]]
    direction = 0
    print(f1(grid, direction))
    print(f2(grid, direction))

