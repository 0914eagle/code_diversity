from typing import List


def sort_numbers(numbers: str) -> str:
    
    num_list = numbers.split()
    num_list.sort(key=lambda x: int(x))
    return ' '.join(num_list)


