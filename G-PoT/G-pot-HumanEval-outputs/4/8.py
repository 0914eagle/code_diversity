
from typing import List

def minPath(grid: List[List[int]], k: int) -> List[int]:
    n = len(grid)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def dfs(curr_path, visited):
        if len(curr_path) == k:
            return curr_path
        
        min_path = None
        for i in range(n):
            for j in range(n):
                if (i, j) not in visited:
                    for dx, dy in directions:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                            new_visited = visited.copy()
                            new_visited.add((i, j))
                            path = dfs(curr_path + [grid[i][j]], new_visited)
                            if min_path is None or path < min_path:
                                min_path = path
        return min_path
    
    return dfs([], set())
