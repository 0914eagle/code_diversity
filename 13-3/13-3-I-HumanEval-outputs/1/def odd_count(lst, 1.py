
from typing import List

def odd_count(lst: List[str]) -> List[str]:
    
    output = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 == 1:
                count += 1
        output.append(f"the number of odd elements {count}n the str{len(string)}ng {len(string)} of the {len(string)}nput.")
    return output

