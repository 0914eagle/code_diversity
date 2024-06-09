
def get_min_days(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    days = 0
    stamina_left = stamina

    # Find the starting and goal positions
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col

    # Breadth-first search to find the shortest path
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if (row, col) == (goal_row, goal_col):
            break
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and (r, c) not in visited:
                queue.append((r, c))
                stamina_left -= 1
                if grid[r][c] == ".":
                    stamina_left -= 1
                elif grid[r][c] == "F":
                    stamina_left -= 2
                elif grid[r][c] == "M":
                    stamina_left -= 3
                if stamina_left <= 0:
                    days += 1
                    stamina_left = stamina

    # Check if the goal is reachable
    if (goal_row, goal_col) not in visited:
        return -1

    # Return the minimum number of days
    return days

