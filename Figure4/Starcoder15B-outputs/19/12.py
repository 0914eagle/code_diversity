from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers_list = numbers.split()
    numbers_list.sort()
    return ' '.join(numbers_list)


