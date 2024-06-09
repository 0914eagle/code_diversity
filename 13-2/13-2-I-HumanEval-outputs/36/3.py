
from typing import List, Tuple

def get_row(lst: List[List[int]], x: int) -> List[Tuple[int, int]]:
    
    result = []
    for i, row in enumerate(lst):
        for j, num in enumerate(row):
            if num == x:
                result.append((i, j))
    return sorted(result, key=lambda x: (x[0], -x[1]))

