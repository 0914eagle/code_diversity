
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
    
    return move_right(grid)

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

def get_final_state(grid, direction):
    
    next_state = get_next_state(grid, direction)
    return merge(next_state)

def main():
    grid = [[int(x) for x in input().split()] for _ in range(4)]
    direction = int(input())
    final_state = get_final_state(grid, direction)
    for row in final_state:
        print(*row)

if __name__ == '__main__':
    main()

