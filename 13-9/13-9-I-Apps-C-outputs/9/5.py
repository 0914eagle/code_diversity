
def get_grid_size(grid):
    return len(grid), len(grid[0])

def get_obstacles(grid):
    obstacles = []
    for row in grid:
        for col in row:
            if col == 'X':
                obstacles.append((row, col))
    return obstacles

def get_conveyor_belts(grid):
    conveyor_belts = []
    for row in grid:
        for col in row:
            if col in ['R', 'L']:
                conveyor_belts.append((row, col))
    return conveyor_belts

def get_points(grid):
    points = []
    for row in grid:
        for col in row:
            if col.isdigit():
                points.append(int(col))
    return points

def set_conveyor_belts(grid, conveyor_belts):
    for row, col in conveyor_belts:
        if grid[row][col] == '?':
            grid[row][col] = 'R'
    return grid

def get_max_score(grid, points):
    max_score = 0
    for point in points:
        max_score += point
    return max_score

def solve(grid):
    grid_size, grid_cols = get_grid_size(grid)
    obstacles = get_obstacles(grid)
    conveyor_belts = get_conveyor_belts(grid)
    points = get_points(grid)
    grid = set_conveyor_belts(grid, conveyor_belts)
    max_score = get_max_score(grid, points)
    return max_score

if __name__ == '__main__':
    grid = [
        ['R', '.', '?', '?', '.'],
        ['.', 'X', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.']
    ]
    print(solve(grid))

