
def can_escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    queue = [(r, c, 0) for r in range(R) for c in range(C) if maze[r][c] == 'J']
    
    while queue:
        r, c, time = queue.pop(0)
        
        if r == 0 or r == R - 1 or c == 0 or c == C - 1:
            return time
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, time + 1))
    
    return "IMPOSSIBLE"

# Read input
R, C = map(int, input().split())
maze = [input() for _ in range(R)]

# Output result
print(can_escape_maze(R, C, maze))
