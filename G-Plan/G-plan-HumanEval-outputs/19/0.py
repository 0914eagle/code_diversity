
from typing import List, Tuple

def find_coordinates(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coordinates = []
    for row_idx, row in enumerate(lst):
        for col_idx, val in enumerate(row):
            if val == x:
                coordinates.append((row_idx, col_idx))
    
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    return find_coordinates(lst, x)

# Input parsing
data = input().strip()
lst = eval(data)
x = int(input().strip())

# Output
result = get_row(lst, x)
print(result)