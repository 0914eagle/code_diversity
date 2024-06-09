
def solve(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    gold_row, gold_col = None, None
    days = 0
    stamina_left = stamina

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
        if (row, col) == (gold_row, gold_col):
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

    # Check if the path is possible
    if stamina_left <= 0:
        return -1

    # Return the number of days needed to reach the gold
    return days

