
from typing import List

def count_water_units(grid: List[List[int]]) -> int:
    return sum(sum(row) for row in grid)

def max_fill(grid: List[List[int]], capacity: int) -> int:
    total_water_units = count_water_units(grid)
    return total_water_units // capacity + (total_water_units % capacity > 0)

if __name__ == "__main__":
    grid = []
    while True:
        try:
            row = list(map(int, input().split()))
            if not row:
                break
            grid.append(row)
        except EOFError:
            break

    capacity = int(input())
    print(max_fill(grid, capacity))
