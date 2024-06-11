from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    if not numbers:
        return []
    if len(numbers) == 1:
        return [numbers[0]]
    if len(numbers) == 2:
        return [max(numbers[0], numbers[1])]
    if len(numbers) == 3:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2])]
    if len(numbers) == 4:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3])]
    if len(numbers) == 5:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3]), max(numbers[3], numbers[4])]
    if len(numbers) == 6:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3]), max(numbers[3], numbers[4]), max(numbers[4], numbers[5])]
    if len(numbers) == 7:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3]), max(numbers[3], numbers[4]), max(numbers[4], numbers[5]), max(numbers[5], numbers[6])]
    if len(numbers) == 8:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3]), max(numbers[3], numbers[4]), max(numbers[4], numbers[5]), max(numbers[5], numbers[6]), max(numbers[6], numbers[7])]
    if len(numbers) == 9:
        return [max(numbers[0], numbers[1]), max(numbers[1], numbers[2]), max(numbers[2], numbers[3]), max(numbers[3], numbers[4]), max(numbers[4], numbers[5]), max(numbers[5], numbers[6]), max(numbers[6], numbers[7]), max(numbers[7], numbers[8])]
    if len(numbers) == 10:
        return [max(numbers[0], numbers[1