from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    
    max_number = numbers[0]
    max_list = [max_number]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
        max_list.append(max_number)
    return max_list

