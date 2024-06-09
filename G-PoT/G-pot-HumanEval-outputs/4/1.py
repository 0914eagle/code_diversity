
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    def dfs(curr_path, curr_pos, visited):
        if len(curr_path) == k:
            return curr_path

        x, y = curr_pos
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        next_paths = []

        for nx, ny in neighbors:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                next_paths.append((nx, ny))

        next_paths.sort(key=lambda pos: grid[pos[0]][pos[1]])

        for np in next_paths:
            visited.add(np)
            res = dfs(curr_path + [grid[np[0]][np[1]]], np, visited)
            if res:
                return res
            visited.remove(np)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            visited.add((i, j))
            res = dfs([grid[i][j]], (i, j), visited)
            if res:
                return res

# Test cases
print(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))  # Output: [1, 2, 1]
print(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1))  # Output: [1]
