alid_path(grid, path):
    rows = len(grid)
    cols = len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols and not visited[row][col]

    def dfs(row, col, index):
        if index == len(path):
            return True

        if not is_valid_move(row, col) or grid[row][col] != path[index]:
            return False

        visited[row][col] = True

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (dr != 0 or dc != 0) and dfs(row + dr, col + dc, index + 1):
                    return True

        visited[row][col] = False
        return False

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True

    return False

def generate_grid(path):
    grid = [['' for _ in range(13)] for _ in range(2)]
    grid[0][0] = path[0]

    for i in range(1, len(path)):
        for r in range(2):
            for c in range(13):
                if grid[r][c] == '':
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if (dr != 0 or dc != 0) and 0 <= r + dr < 2 and 0 <= c + dc < 13:
                                if grid[r + dr][c + dc] == '' and (r + dr != r or c + dc != c):
                                    grid[r + dr][c + dc] = path[i]
                                    break
                    break

    return grid

def find_grid(s):
    path = s
    grid = generate_grid(path)

    if is_valid_path(grid, path):
        return grid
    else:
        return "Impossible"

if __name__ == "__main__":
    s = input().strip()
    result = find_grid(s)

    if result == "Impossible":
        print("Impossible")
    else:
        for row in result:
            print(''.join(row))
