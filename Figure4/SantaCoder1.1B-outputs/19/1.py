from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers = numbers.split()
    numbers.sort(key=int)
    return ' '.join(map(str, numbers))


