
from collections import deque

def escape_maze(R, C, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def is_valid_move(row, col):
        return 0 <= row < R and 0 <= col < C
    
    def bfs():
        queue = deque([(j_row, j_col, 0)])
        visited = set()
        
        while queue:
            row, col, time = queue.popleft()
            
            if row == 0 or row == R - 1 or col == 0 or col == C - 1:
                return time
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                if is_valid_move(new_row, new_col) and maze[new_row][new_col] == '.' and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col, time + 1))
                    visited.add((new_row, new_col))
        
        return -1
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                j_row, j_col = i, j
    
    escape_time = bfs()
    
    if escape_time == -1:
        return "IMPOSSIBLE"
    else:
        return escape_time

# Read input
R, C = map(int, input().split())
maze = [input() for _ in range(R)]

# Solve the problem
result = escape_maze(R, C, maze)
print(result)
