
from typing import List

def calculate_total_water(grid: List[List[int]]) -> int:
    return sum(sum(row) for row in grid)

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_water = calculate_total_water(grid)
    return (total_water + capacity - 1) // capacity

if __name__ == "__main__":
    grid = eval(input())
    capacity = int(input())
    print(max_fill(grid, capacity))
