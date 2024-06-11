from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    if len(numbers) == 1:
        return numbers
    if len(numbers) == 2:
        return [max(numbers)]
    if len(numbers) == 3:
        return [max(numbers), max(numbers)]
    if len(numbers) == 4:
        return [max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 5:
        return [max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 6:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 7:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 8:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 9:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 10:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 11:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 12:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 13:
        return [max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers), max(numbers)]
    if len(numbers) == 14:
        return [max(numbers), max