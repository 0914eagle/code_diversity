
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    def is_valid_move(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def backtrack(row, col, path, visited):
        if len(path) == k:
            nonlocal min_path
            if not min_path or path < min_path:
                min_path = path[:]
            return

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                backtrack(new_row, new_col, path + [grid[new_row][new_col]], visited)
                visited.remove((new_row, new_col))

    min_path = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            visited.add((i, j))
            backtrack(i, j, [grid[i][j]], visited)

    return min_path

# Read input
grid = [[int(num) for num in input().split()] for _ in range(len(input().split()))]
k = int(input())

# Call the function and print the result
print(minPath(grid, k))
