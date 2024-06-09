
def can_escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid_move(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def spread_fire(fire_positions):
        new_fire_positions = set()
        for x, y in fire_positions:
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if is_valid_move(new_x, new_y) and maze[new_x][new_y] == '.':
                    maze[new_x][new_y] = 'F'
                    new_fire_positions.add((new_x, new_y))
        return new_fire_positions
    
    def find_neighbors(x, y):
        neighbors = []
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                neighbors.append((new_x, new_y))
        return neighbors
    
    def bfs():
        queue = [(joe_x, joe_y, 0)]
        visited = set()
        
        while queue:
            x, y, time = queue.pop(0)
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return time
            
            for nx, ny in find_neighbors(x, y):
                if maze[nx][ny] == '.' and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, time + 1))
        
            fire_positions = spread_fire(fire_positions)
            if any((x, y) in fire_positions for x, y, _ in queue):
                return "IMPOSSIBLE"
        
        return "IMPOSSIBLE"
    
    fire_positions = set()
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'F':
                fire_positions.add((i, j))
            elif maze[i][j] == 'J':
                joe_x, joe_y = i, j
    
    return bfs()

# Read input
R, C = map(int, input().split())
maze = [list(input()) for _ in range(R)]

# Solve the problem
result = can_escape_maze(R, C, maze)

# Print the result
print(result)
