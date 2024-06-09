
from typing import List

def odd_count(lst: List[str]) -> List[str]:
    
    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 == 1:
                count += 1
        result.append(f"the number of odd elements {count}n the str{len(string)}ng {len(string)} of the {len(string)}nput.")
    return result

