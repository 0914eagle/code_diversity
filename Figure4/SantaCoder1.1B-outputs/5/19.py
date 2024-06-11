from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    
    return numbers[0::2] + [delimeter] + numbers[1::2]
