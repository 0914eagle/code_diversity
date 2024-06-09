
def get_min_days(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    end_row, end_col = None, None
    days = 0
    stamina_left = stamina

    # Find the starting and ending positions
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                end_row, end_col = row, col

    # Breadth-first search to find the shortest path
    queue = [(start_row, start_col, stamina_left)]
    visited = set()
    while queue:
        row, col, stamina = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if (row, col) == (end_row, end_col):
            return days
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#":
                cost = 1 if grid[r][c] == "." else 2 if grid[r][c] == "F" else 3
                if stamina - cost >= 0:
                    queue.append((r, c, stamina - cost))
        stamina_left = stamina
        days += 1

    return -1

