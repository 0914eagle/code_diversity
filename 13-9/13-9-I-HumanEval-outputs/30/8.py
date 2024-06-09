
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    
    seen: set[int] = set()
    result: list[int] = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result

