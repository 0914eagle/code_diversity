
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # your code here
    new_list = []
    for word in lst:
        if len(word) % 2 == 0:
            new_list.append(word)
    new_list.sort(key=len)
    new_list.sort()
    return new_list

