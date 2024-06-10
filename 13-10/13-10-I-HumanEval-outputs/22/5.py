
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # Delete strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort list by length and then alphabetically if length is the same
    lst.sort(key=lambda x: (len(x), x))
    
    return lst

