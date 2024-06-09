
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    rows, cols = len(grid), len(grid[0])
    wells = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                wells[i][j] = 1
    buckets = capacity
    count = 0
    while buckets > 0 and any(wells):
        for i in range(rows):
            for j in range(cols):
                if wells[i][j] == 1 and buckets > 0:
                    wells[i][j] = 0
                    buckets -= 1
        count += 1
    return count

