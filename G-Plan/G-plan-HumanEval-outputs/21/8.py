
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_water = sum(sum(row) for row in grid)
    return (total_water + capacity - 1) // capacity

if __name__ == "__main__":
    grid = eval(input())
    capacity = int(input())
    print(max_fill(grid, capacity))
