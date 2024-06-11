from typing import List


def sort_numbers(numbers: str) -> str:
    
    num_dict = {
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
    num_list = numbers.split()
    num_list.sort(key=lambda x: num_dict[x])
    return ' '.join(num_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/tests/test_sort_numbers.py
import unittest
from sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    