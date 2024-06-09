
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def dfs(x, y, path):
        if len(path) == k:
            return path
        
        min_path = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in path:
                new_path = dfs(nx, ny, path + [(nx, ny)])
                if not min_path or new_path < min_path:
                    min_path = new_path
        
        return min_path
    
    min_path = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [(i, j)])
            if not min_path or path < min_path:
                min_path = path
    
    return [grid[x][y] for x, y in min_path]

# Test cases
print(minPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3))  # Output: [1, 2, 1]
print(minPath([[5, 9, 3], [4, 1, 6], [7, 8, 2]], 1))  # Output: [1]
