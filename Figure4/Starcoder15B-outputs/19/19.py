from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers = numbers.split()
    numbers = [int(num) for num in numbers]
    numbers.sort()
    numbers = [str(num) for num in numbers]
    return ' '.join(numbers)


