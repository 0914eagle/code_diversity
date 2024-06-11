from typing import List


def sort_numbers(numbers: str) -> str:
    
    numbers_list = numbers.split()
    numbers_list.sort(key=lambda x: ord(x) - ord('a'))
    return ' '.join(numbers_list)


if __name__ == "__