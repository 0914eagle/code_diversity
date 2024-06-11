from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: int(x[::-1].replace('zero', '0').replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9')))
    return ' '.join(numbers_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
/python/exercises/ex001/test_ex001.py
from ex001 import sort_numbers


