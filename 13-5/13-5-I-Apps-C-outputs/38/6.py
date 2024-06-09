
def solve(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    goal_row, goal_col = None, None
    days = 0
    stamina_spent = 0

    # Find the starting and goal positions
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                goal_row, goal_col = row, col

    # Breadth-first search to find the shortest path to the goal
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if row == goal_row and col == goal_col:
            break
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and (r, c) not in visited:
                queue.append((r, c))
                stamina_spent += 1
                if stamina_spent > stamina:
                    days += 1
                    stamina_spent = 0

    # Check if a path exists
    if row != goal_row or col != goal_col:
        return -1

    # Calculate the number of days needed to reach the goal
    while stamina_spent > 0:
        days += 1
        stamina_spent -= stamina

    return days

