
def escape_maze(R, C, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid_move(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def bfs():
        queue = []
        visited = set()
        
        for i in range(R):
            for j in range(C):
                if maze[i][j] == 'J':
                    queue.append((i, j, 0))
                    visited.add((i, j))
                elif maze[i][j] == 'F':
                    queue.append((i, j, float('inf')))
                    visited.add((i, j))
        
        while queue:
            x, y, time = queue.pop(0)
            
            if time == float('inf'):
                continue
            
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return time
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                
                if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited and maze[new_x][new_y] != '#':
                    queue.append((new_x, new_y, time + 1))
                    visited.add((new_x, new_y))
        
        return "IMPOSSIBLE"
    
    return bfs()

# Read input
R, C = map(int, input().split())
maze = [input() for _ in range(R)]

# Solve the maze and print the output
print(escape_maze(R, C, maze))
