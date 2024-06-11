from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers = numbers.split()
    numbers.sort()
    return ' '.join(numbers)


