from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    if not numbers:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(numbers[i])
        result.append(delimeter)
    return result


if