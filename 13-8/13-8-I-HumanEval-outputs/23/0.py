
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
    return count

