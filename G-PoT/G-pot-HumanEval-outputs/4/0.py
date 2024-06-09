
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, path):
        if len(path) == k:
            return path

        current_val = grid[x][y]
        grid[x][y] = -1  # Mark cell as visited

        next_moves = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:
                next_moves.append((nx, ny))

        next_moves.sort(key=lambda pos: grid[pos[0]][pos[1]])

        for nx, ny in next_moves:
            result = dfs(nx, ny, path + [current_val])
            if result:
                return result

        grid[x][y] = current_val  # Reset cell value if no valid path found
        return None

    for i in range(n):
        for j in range(n):
            result = dfs(i, j, [])
            if result:
                return result
