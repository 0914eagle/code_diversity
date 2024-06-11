from typing import List


def sort_numbers(numbers: str) -> str:
    
    num_list = numbers.split()
    num_list.sort(key=lambda x: ord(x[0]))
    return ' '.join(num_list)


