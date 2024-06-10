
def get_map_info(map_grid):
    n_rows, n_cols = len(map_grid), len(map_grid[0])
    start_row, start_col = None, None
    treasure_row, treasure_col = None, None
    for row in range(n_rows):
        for col in range(n_cols):
            if map_grid[row][col] == 'S':
                start_row, start_col = row, col
            elif map_grid[row][col] == 'G':
                treasure_row, treasure_col = row, col
    return n_rows, n_cols, start_row, start_col, treasure_row, treasure_col

def get_min_days(map_grid, k):
    n_rows, n_cols, start_row, start_col, treasure_row, treasure_col = get_map_info(map_grid)
    visited = [[False for _ in range(n_cols)] for _ in range(n_rows)]
    queue = [(start_row, start_col, 0)]
    while queue:
        row, col, days = queue.pop(0)
        if visited[row][col]:
            continue
        visited[row][col] = True
        if row == treasure_row and col == treasure_col:
            return days
        for r, c in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            if 0 <= r < n_rows and 0 <= c < n_cols and not visited[r][c] and map_grid[r][c] != '#':
                queue.append((r, c, days+1))
    return -1

def main():
    map_grid = [
        ['.', '.', '.', '.', '#', '.'],
        ['.', 'M', 'F', 'F', '.', '.'],
        ['.', '.', '.', '#', '.', 'G']
    ]
    k = 4
    print(get_min_days(map_grid, k))

if __name__ == '__main__':
    main()

