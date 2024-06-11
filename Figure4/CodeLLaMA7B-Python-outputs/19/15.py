from typing import List


def sort_numbers(numbers: str) -> str:
    
    if numbers == '':
        return ''
    nums = numbers.split()
    nums.sort(key=lambda x: int(nums_dict[x]))
    return ' '.join(nums)


nums_dict = {
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


