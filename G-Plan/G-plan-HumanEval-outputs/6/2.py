
from typing import List
import re

def count_odd_digits(s: str) -> int:
    return sum(1 for c in s if c in '13579')

def odd_count(lst: List[str]) -> List[str]:
    output = []
    for s in lst:
        count = count_odd_digits(s)
        output.append(f'the number of odd elements {count}n the str{count}ng {count} of the {count}nput.')
    return output

if __name__ == "__main__":
    input_list = input().strip().split(',')
    result = odd_count(input_list)
    for res in result:
        print(res)
