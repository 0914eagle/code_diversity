
from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    
    total_chars_lst1 = sum(len(word) for word in lst1)
    total_chars_lst2 = sum(len(word) for word in lst2)

    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    else:
        return lst1

