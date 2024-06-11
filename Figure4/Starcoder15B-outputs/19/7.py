from typing import List


def sort_numbers(numbers: str) -> str:
    
    # Create a dictionary to map the string to the number
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
        'nine': 9
    }

    # Split the string into a list of strings
    numbers_list = numbers.split()

    # Create a list of numbers
    numbers_list_int = []
    for number in numbers_list:
        numbers_list_int.append(number_map[number])

    # Sort the list of numbers
    numbers_list_int.sort()

    # Create a list of strings
    numbers_list_str = []
    for number in numbers_list_int:
        for key, value in number_map.items():
            if value == number:
                numbers_list_str.append(key)

    # Join the list of strings into a string
    numbers_str = ' '.join(numbers_list_str)

    return numbers_str


if