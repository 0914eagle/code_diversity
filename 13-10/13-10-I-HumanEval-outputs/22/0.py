
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # Delete strings with odd lengths from the list
    odd_lengths = [word for word in lst if len(word) % 2 == 1]
    lst = [word for word in lst if word not in odd_lengths]
    
    # Sort the list by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    
    return lst

