from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers = numbers.split()
    numbers = [int(x) for x in numbers]
    numbers.sort()
    numbers = [str(x) for x in numbers]
    return ' '.join(numbers)


