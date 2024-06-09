
def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def is_valid_move(x, y):
        return 0 <= x < n and 0 <= y < n

    def dfs(x, y, path):
        if len(path) == k:
            return path

        current_val = grid[x][y]
        grid[x][y] = -1  # Mark cell as visited

        next_moves = []
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and grid[new_x][new_y] != -1:
                next_moves.append((new_x, new_y))

        next_moves.sort(key=lambda move: grid[move[0]][move[1]])

        for next_x, next_y in next_moves:
            result = dfs(next_x, next_y, path + [current_val])
            if result:
                return result

        grid[x][y] = current_val  # Reset cell value if path not found
        return None

    for i in range(n):
        for j in range(n):
            result = dfs(i, j, [])
            if result:
                return result
