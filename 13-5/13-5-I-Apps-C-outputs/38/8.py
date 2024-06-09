
def find_treasure(grid, stamina):
    # Initialize variables
    rows, cols = len(grid), len(grid[0])
    start_row, start_col = None, None
    end_row, end_col = None, None
    days = 0
    stamina_used = 0
    
    # Find the starting and ending positions
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "S":
                start_row, start_col = row, col
            elif grid[row][col] == "G":
                end_row, end_col = row, col
    
    # Breadth-first search to find the shortest path
    queue = [(start_row, start_col)]
    visited = set()
    while queue:
        row, col = queue.pop(0)
        visited.add((row, col))
        if (row, col) == (end_row, end_col):
            break
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#" and (r, c) not in visited:
                queue.append((r, c))
                stamina_used += 1
                if stamina_used > stamina:
                    days += 1
                    stamina_used = 0
    
    # Check if the path is possible with the given stamina
    if (end_row, end_col) not in visited:
        return -1
    
    # Return the number of days needed to reach the treasure
    return days + 1

