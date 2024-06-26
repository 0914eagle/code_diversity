
from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    
    if len(lst1) == 0 or len(lst2) == 0:
        return []

    total_len1 = sum(len(s) for s in lst1)
    total_len2 = sum(len(s) for s in lst2)

    if total_len1 < total_len2:
        return lst1
    elif total_len1 > total_len2:
        return lst2
    else:
        return lst1

