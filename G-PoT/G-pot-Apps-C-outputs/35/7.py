
def can_escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = []
    visited = set()
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'J':
                queue.append((i, j, 0))
                visited.add((i, j))
            if maze[i][j] == 'F':
                queue.append((i, j, float('inf')))
                visited.add((i, j))
    
    while queue:
        i, j, time = queue.pop(0)
        
        if time == float('inf') and (i == 0 or i == R-1 or j == 0 or j == C-1):
            return "IMPOSSIBLE"
        
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < R and 0 <= y < C and maze[x][y] != '#' and (x, y) not in visited:
                visited.add((x, y))
                queue.append((x, y, time + 1))
    
    return time

# Read input
R, C = map(int, input().split())
maze = [input() for _ in range(R)]

# Call the function and print the output
print(can_escape_maze(R, C, maze))
