
from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    
    # Delete the strings with odd lengths
    lst = [word for word in lst if len(word) % 2 == 0]
    
    # Sort the list by length and then alphabetically
    lst.sort(key=lambda x: (len(x), x))
    
    return lst

