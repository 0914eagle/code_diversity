
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    
    rows, cols = len(grid), len(grid[0])
    wells = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            wells[i][j] = grid[i][j]
    total_water = sum(sum(row) for row in wells)
    if total_water == 0:
        return 0
    buckets = capacity
    num_lowers = 0
    while total_water > 0:
        for i in range(rows):
            for j in range(cols):
                if wells[i][j] > 0:
                    if buckets > wells[i][j]:
                        buckets -= wells[i][j]
                        wells[i][j] = 0
                        total_water -= wells[i][j]
                    else:
                        wells[i][j] -= buckets
                        total_water -= buckets
                        buckets = 0
        num_lowers += 1
    return num_lowers

