
from typing import List, Tuple

def find_coordinates(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    coordinates = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                coordinates.append((i, j))
    return sorted(coordinates, key=lambda coord: (coord[0], -coord[1]))

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    return find_coordinates(lst, x)

# Input parsing
input_list = eval(input())
x = int(input())

# Output
print(get_row(input_list, x))
