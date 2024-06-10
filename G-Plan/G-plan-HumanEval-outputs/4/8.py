
from typing import List
from queue import PriorityQueue

def minPath(grid: List[List[int]], k: int) -> List[int]:
    def is_valid_move(row, col, visited):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and (row, col) not in visited

    def backtrack(row, col, path, visited):
        if len(path) == k:
            nonlocal min_path
            if not min_path or path < min_path:
                min_path = path[:]
            return

        visited.add((row, col))
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col, visited):
                backtrack(new_row, new_col, path + [grid[new_row][new_col]], visited)
        visited.remove((row, col))

    min_path = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            backtrack(i, j, [grid[i][j]], visited)

    return min_path

# Read input
grid = []
while True:
    try:
        row = list(map(int, input().split()))
        grid.append(row)
    except EOFError:
        break

k = int(input())

# Call the function and print the result
print(minPath(grid, k))
