
def get_min_days(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    gold_row, gold_col = None, None
    days = 0
    stamina_used = 0

    # Find the starting and gold locations
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                gold_row, gold_col = row, col

    # Breadth-first search to find the shortest path to the gold
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if grid[row][col] == "G":
            break
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] != "#":
                queue.append((r, c))
                stamina_used += 1
                if stamina_used > stamina:
                    days += 1
                    stamina_used = 0

    # Check if the gold is reachable
    if grid[gold_row][gold_col] == "#":
        return -1

    # Return the minimum number of days
    return days + 1

