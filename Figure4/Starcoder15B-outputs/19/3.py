from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers = numbers.split()
    numbers = [int(number) for number in numbers]
    numbers.sort()
    numbers = [str(number) for number in numbers]
    return ' '.join(numbers)


