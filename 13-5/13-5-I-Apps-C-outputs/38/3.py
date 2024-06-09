
def solve(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    days = 0
    stamina_spent = 0
    queue = []

    # Find the starting and goal positions
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col

    # Breadth-first search to find the shortest path
    queue.append((start_row, start_col, 0))
    visited = set()
    while queue:
        row, col, day = queue.pop(0)
        if (row, col) == (goal_row, goal_col):
            return day
        visited.add((row, col))
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and (r, c) not in visited:
                queue.append((r, c, day+1))

    # If the goal is not reachable, return -1
    return -1

