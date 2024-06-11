from typing import List


def parse_music(music_string: str) -> List[int]:
    
    return [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]


if __name__ == '__main__':
    print(parse_music('o o| .| o| o| .| .| .| .| o o'))
/01_basics/01_basics.py
# 1.1
# Write a function that takes a list of numbers and returns a new list that contains only the even numbers.
#
# >>> even_numbers([1, 2, 3, 4, 5, 6])
# [2, 4, 6]
# >>> even_numbers([1, 3, 5])
# []
# >>> even_numbers([])
# []
# >>> even_numbers([-2, -4, -6])
# [-2, -4, -6]

