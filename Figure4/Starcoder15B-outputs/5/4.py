from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    if not numbers:
        return []
    return numbers[:1] + [delimeter] + intersperse(numbers[1:], delimeter)


if