
from typing import List
import re

def count_odd_digits(s: str) -> int:
    return sum(1 for digit in s if int(digit) % 2 != 0)

def odd_count(lst: List[str]) -> List[str]:
    result = []
    for s in lst:
        odd_count = count_odd_digits(s)
        result.append(f"the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.")
    return result

if __name__ == "__main__":
    input_list = input().strip().split()
    output = odd_count(input_list)
    for line in output:
        print(line)
