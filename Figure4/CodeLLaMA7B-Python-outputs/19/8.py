from typing import List


def sort_numbers(numbers: str) -> str:
    
    # split the string into a list of numbers
    numbers_list = numbers.split()
    # sort the list
    numbers_list.sort()
    # return the list as a string
    return " ".join(numbers_list)


