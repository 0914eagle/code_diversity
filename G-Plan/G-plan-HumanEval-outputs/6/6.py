
from typing import List
import re

def count_odd_digits(s: str) -> int:
    return len(re.findall('[13579]', s))

def odd_count(lst: List[str]) -> List[str]:
    def replace_i(s: str, count: int) -> str:
        return s.replace('i', str(count))

    result = []
    for string in lst:
        odd_count = count_odd_digits(string)
        result.append(replace_i('the number of odd elements in the string i of the input.', odd_count))
    
    return result

if __name__ == "__main__":
    input_list = input().strip()[1:-1].split(', ')
    output = odd_count(input_list)
    print(output)
