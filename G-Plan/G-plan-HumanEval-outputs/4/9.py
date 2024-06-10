
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int:
    def is_valid_move(x, y, visited):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) not in visited

    def backtrack(x, y, path, visited):
        if len(path) == k:
            nonlocal min_path
            if not min_path or path < min_path:
                min_path = path[:]
            return

        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y, visited):
                path.append(grid[new_x][new_y])
                backtrack(new_x, new_y, path, visited)
                path.pop()

        visited.remove((x, y))

    min_path = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            path = [grid[i][j]]
            backtrack(i, j, path, visited)

    return min_path

# Read input
grid = [[int(x) for x in input().split()] for _ in range(len(grid))]
k = int(input())

# Call the function and print the result
print(minPath(grid, k))
