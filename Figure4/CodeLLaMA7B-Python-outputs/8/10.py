from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    return sum(numbers), 1 if not numbers else 1 * (a * b for a, b in zip(numbers, numbers[1:]))


if