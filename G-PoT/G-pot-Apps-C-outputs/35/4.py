
def can_escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid_move(row, col):
        return 0 <= row < R and 0 <= col < C
    
    def spread_fire(fire_positions):
        new_fire_positions = set()
        for row, col in fire_positions:
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if is_valid_move(new_row, new_col) and maze[new_row][new_col] == '.':
                    maze[new_row][new_col] = 'F'
                    new_fire_positions.add((new_row, new_col))
        return new_fire_positions
    
    def bfs():
        queue = [(j_row, j_col, 0)]
        visited = set()
        
        while queue:
            row, col, time = queue.pop(0)
            
            if row == 0 or row == R - 1 or col == 0 or col == C - 1:
                return time
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if is_valid_move(new_row, new_col) and (new_row, new_col) not in visited and maze[new_row][new_col] == '.':
                    queue.append((new_row, new_col, time + 1))
                    visited.add((new_row, new_col))
        
        return -1
    
    j_row, j_col = -1, -1
    fire_positions = set()
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                j_row, j_col = i, j
            elif maze[i][j] == 'F':
                fire_positions.add((i, j))
    
    maze[j_row][j_col] = '.'
    
    time = 0
    while True:
        if j_row == 0 or j_row == R - 1 or j_col == 0 or j_col == C - 1:
            return time
        
        if not fire_positions:
            return -1
        
        fire_positions = spread_fire(fire_positions)
        time += 1
        
        escape_time = bfs()
        if escape_time != -1:
            return escape_time
    
    return -1

# Read input
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

# Solve the problem
result = can_escape_maze(R, C, maze)

# Output the result
if result == -1:
    print("IMPOSSIBLE")
else:
    print(result)
