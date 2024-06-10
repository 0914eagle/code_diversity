
from typing import List
import re

def count_odd_digits(s: str) -> int:
    return sum(1 for c in s if c in '13579')

def odd_count(lst: List[str]) -> List[str]:
    def replace_i(template, count):
        return template.replace('i', str(count))

    output = []
    template = 'the number of odd elements in the string i of the input.'
    
    for s in lst:
        odd_count = count_odd_digits(s)
        output.append(replace_i(template, odd_count))
    
    return output

if __name__ == "__main__":
    input_list = input().strip().split(',')
    result = odd_count(input_list)
    for res in result:
        print(res)
