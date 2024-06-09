
from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    
    # Sort the list
    lst.sort()
    # Check if the list has at least 2 elements
    if len(lst) < 2:
        return None
    # Return the 2nd smallest element
    return lst[1]

