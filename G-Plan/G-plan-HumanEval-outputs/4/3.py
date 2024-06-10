
from typing import List
from queue import PriorityQueue

def minPath(grid: List[List[int]], k: int) -> List[int]:
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def backtrack(curr_path, visited, x, y):
        if len(curr_path) == k:
            nonlocal min_path
            if not min_path or curr_path < min_path:
                min_path = curr_path[:]
            return

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                curr_path.append(grid[new_x][new_y])
                backtrack(curr_path, visited, new_x, new_y)
                curr_path.pop()
                visited.remove((new_x, new_y))

    min_path = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            visited = set()
            visited.add((i, j))
            backtrack([grid[i][j]], visited, i, j)

    return min_path

# Read input
grid = []
while True:
    try:
        row = list(map(int, input().strip().split()))
        grid.append(row)
    except EOFError:
        break

k = int(input().strip())

# Call the function and print the result
print(minPath(grid, k))
