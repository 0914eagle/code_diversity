from typing import List


def sort_numbers(numbers: str) -> str:
    
    if numbers == '':
        return ''
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: int(x))
    return ' '.join(numbers_list)


