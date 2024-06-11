from typing import List


def sort_numbers(numbers: str) -> str:
    
    number_map = {
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
    numbers = numbers.split(' ')
    numbers = [number_map[number] for number in numbers]
    numbers.sort()
    numbers = [list(number_map.keys())[list(number_map.values()).index(number)] for number in numbers]
    return ' '.join(numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/tests/test_sort_numbers.py
import unittest
from sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    