from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    return sum(numbers), reduce(lambda x, y: x * y, numbers, 1)


if