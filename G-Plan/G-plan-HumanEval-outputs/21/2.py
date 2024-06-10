
from typing import List

def count_water_units(grid: List[List[int]]) -> int:
    return sum(sum(row) for row in grid)

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_water = count_water_units(grid)
    return total_water // capacity + (total_water % capacity > 0)

if __name__ == "__main__":
    grid = eval(input())
    capacity = int(input())
    print(max_fill(grid, capacity))
