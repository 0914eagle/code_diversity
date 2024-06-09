
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # your code here
    return sorted(lst, key=lambda x: (-len(x), x))

