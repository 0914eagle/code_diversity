from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return [delimeter if i % 2 == 1 else number for i, number in enumerate(numbers)]


if