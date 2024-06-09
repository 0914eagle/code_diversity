
def escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid_move(row, col):
        return 0 <= row < R and 0 <= col < C
    
    def spread_fire(fire_positions):
        new_fire_positions = []
        for row, col in fire_positions:
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if is_valid_move(new_row, new_col) and maze[new_row][new_col] == '.':
                    maze[new_row][new_col] = 'F'
                    new_fire_positions.append((new_row, new_col))
        return new_fire_positions
    
    def can_escape(row, col):
        visited = set()
        queue = [(row, col, 0)]
        
        while queue:
            r, c, time = queue.pop(0)
            if (r == 0 or r == R - 1 or c == 0 or c == C - 1) and maze[r][c] != 'F':
                return time
            
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if is_valid_move(new_r, new_c) and maze[new_r][new_c] != '#' and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c, time + 1))
        
        return float('inf')
    
    fire_positions = [(r, c) for r in range(R) for c in range(C) if maze[r][c] == 'F']
    
    time = 0
    while fire_positions:
        fire_positions = spread_fire(fire_positions)
        time += 1
        if time >= R + C:
            return "IMPOSSIBLE"
    
    for r in range(R):
        for c in range(C):
            if maze[r][c] == 'J':
                return can_escape(r, c)

# Read input
R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

# Call the function and print the result
print(escape_maze(R, C, maze))
