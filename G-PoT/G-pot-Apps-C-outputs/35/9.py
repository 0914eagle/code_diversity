
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
    
    def find_neighbors(row, col):
        neighbors = []
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col) and maze[new_row][new_col] != '#':
                neighbors.append((new_row, new_col))
        return neighbors
    
    def bfs():
        queue = [(j_row, j_col, 0)]
        visited = set()
        visited.add((j_row, j_col))
        
        while queue:
            row, col, time = queue.pop(0)
            
            if row == 0 or row == R - 1 or col == 0 or col == C - 1:
                return time
            
            for neighbor_row, neighbor_col in find_neighbors(row, col):
                if (neighbor_row, neighbor_col) not in visited:
                    queue.append((neighbor_row, neighbor_col, time + 1))
                    visited.add((neighbor_row, neighbor_col))
        
        return float('inf')
    
    fire_positions = set()
    j_row, j_col = -1, -1
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_positions.add((i, j))
            elif maze[i][j] == 'J':
                j_row, j_col = i, j
    
    time = 0
    while j_row != -1 and time < R * C:
        if j_row == 0 or j_row == R - 1 or j_col == 0 or j_col == C - 1:
            return time
        
        fire_positions = spread_fire(fire_positions)
        time += 1
        
        if (j_row, j_col) in fire_positions:
            return "IMPOSSIBLE"
        
        time_to_exit = bfs()
        if time_to_exit != float('inf'):
            return time + time_to_exit
        
    return "IMPOSSIBLE"

# Read input
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

# Solve the problem
result = can_escape_maze(R, C, maze)
print(result)
