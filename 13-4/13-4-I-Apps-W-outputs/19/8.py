
def f1(maze):
    # f1() function to find the maximum possible number of moves Aoki has to make
    # maze is a 2D list representing the maze
    
    # Initialize variables
    max_moves = 0
    start_row, start_col = 0, 0
    goal_row, goal_col = 0, 0
    
    # Find the starting and goal squares
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start_row, start_col = row, col
            if maze[row][col] == 'G':
                goal_row, goal_col = row, col
    
    # Breadth-first search to find the maximum number of moves
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        if (row, col) not in visited:
            visited.add((row, col))
            if (row, col) == (goal_row, goal_col):
                return max_moves
            for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == '.':
                    queue.append((r, c))
            max_moves += 1
    
    return max_moves

def f2(maze):
    # f2() function to find the minimum number of moves Aoki has to make
    # maze is a 2D list representing the maze
    
    # Initialize variables
    min_moves = 0
    start_row, start_col = 0, 0
    goal_row, goal_col = 0, 0
    
    # Find the starting and goal squares
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start_row, start_col = row, col
            if maze[row][col] == 'G':
                goal_row, goal_col = row, col
    
    # Depth-first search to find the minimum number of moves
    visited = set()
    def dfs(row, col, moves):
        nonlocal min_moves
        if (row, col) in visited:
            return
        visited.add((row, col))
        if (row, col) == (goal_row, goal_col):
            min_moves = moves
            return
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == '.':
                dfs(r, c, moves+1)
    
    dfs(start_row, start_col, 0)
    return min_moves

if __name__ == '__main__':
    H, W = map(int, input().split())
    maze = [input() for _ in range(H)]
    print(f1(maze))
    print(f2(maze))

