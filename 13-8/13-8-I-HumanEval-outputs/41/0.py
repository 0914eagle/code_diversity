
from typing import List

def total_match(lst1: List[str], lst2: List[str]) -> List[str]:
    
    # Calculate the total number of chars in both lists
    total_chars_lst1 = sum(len(word) for word in lst1)
    total_chars_lst2 = sum(len(word) for word in lst2)

    # Check if the total number of chars in lst1 is less than lst2
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    # Check if the total number of chars in lst2 is less than lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    # If the two lists have the same number of chars, return the first list
    else:
        return lst1

