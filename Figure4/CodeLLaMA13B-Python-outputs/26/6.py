from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    
    return list(dict.fromkeys(numbers))


if