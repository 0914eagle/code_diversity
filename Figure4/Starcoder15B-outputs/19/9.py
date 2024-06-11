from typing import List


def sort_numbers(numbers: str) -> str:
    
    # TODO: Implement this function
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    numbers.sort()
    numbers = [str(i) for i in numbers]
    return " ".join(numbers)


