
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    rows, cols = len(grid), len(grid[0])
    wells = [[0] * cols for _ in range(rows)]
    buckets = [0] * cols
    count = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                wells[i][j] = 1

    for j in range(cols):
        for i in range(rows):
            if wells[i][j] == 1:
                if buckets[j] + wells[i][j] <= capacity:
                    buckets[j] += wells[i][j]
                    wells[i][j] = 0
                    count += 1

    return count

