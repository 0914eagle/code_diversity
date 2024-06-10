
from typing import List
import re

def count_odd_digits(s: str) -> int:
    return sum(1 for char in s if char in '13579')

def odd_count(lst: List[str]) -> List[str]:
    def replace_i_template(s: str, count: int) -> str:
        return s.replace('i', str(count))

    output = []
    for string in lst:
        odd_count = count_odd_digits(string)
        output.append(replace_i_template('the number of odd elements in the string i of the input.', odd_count))
    
    return output

if __name__ == "__main__":
    input_strings = input().strip().split()
    result = odd_count(input_strings)
    for res in result:
        print(res)
