
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # your code here
    result = []
    for word in lst:
        if len(word) % 2 == 0:
            result.append(word)
    result.sort(key=len)
    result.sort()
    return result

