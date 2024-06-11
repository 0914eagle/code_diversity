from typing import List


def sort_numbers(numbers: str) -> str:
    
    number_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    numbers = numbers.split()
    numbers = [number_dict[number] for number in numbers]
    numbers.sort()
    numbers = [list(number_dict.keys())[list(number_dict.values()).index(number)] for number in numbers]
    return ' '.join(numbers)


if