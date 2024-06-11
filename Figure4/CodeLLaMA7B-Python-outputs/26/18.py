from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    seen = set()
    result = []
    for number in numbers:
        if number not in seen:
            result.append(number)
            seen.add(number)
    return result


if