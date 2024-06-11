from typing import List


def sort_numbers(numbers: str) -> str:
    
    # split the string into a list of numbers
    num_list = numbers.split()
    # sort the list
    num_list.sort()
    # join the list back into a string
    return " ".join(num_list)


