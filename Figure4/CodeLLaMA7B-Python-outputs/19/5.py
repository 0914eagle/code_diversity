from typing import List


def sort_numbers(numbers: str) -> str:
    
    # split string into list
    num_list = numbers.split()
    # sort list
    num_list.sort()
    # join list into string
    return " ".join(num_list)


