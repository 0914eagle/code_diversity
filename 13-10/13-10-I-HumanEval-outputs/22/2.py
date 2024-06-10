
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # your code here
    odd_lengths = [word for word in lst if len(word) % 2 == 1]
    return sorted(set(lst) - set(odd_lengths))

