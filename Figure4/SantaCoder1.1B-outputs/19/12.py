from typing import List


def sort_numbers(numbers: str) -> str:
    
    # TODO: Write your code here
    numbers = numbers.split()
    numbers.sort()
    return ' '.join(numbers)


