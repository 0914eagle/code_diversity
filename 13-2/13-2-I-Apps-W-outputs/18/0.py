
def get_max_moves(maze):
    # Initialize variables
    max_moves = 0
    start_row, start_col = 0, 0
    end_row, end_col = 0, 0

    # Find the starting and ending squares
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 'S':
                start_row, start_col = row, col
            if maze[row][col] == 'G':
                end_row, end_col = row, col

    # Breadth-first search to find the maximum number of moves
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if row == end_row and col == end_col:
            return len(visited) - 1
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == '.' and (r, c) not in visited:
                queue.append((r, c))

    return max_moves

