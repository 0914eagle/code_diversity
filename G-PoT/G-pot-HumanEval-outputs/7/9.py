
from typing import List

def by_length(arr: List[int]) -> List[str]:
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    filtered_arr = [x for x in arr if 1 <= x <= 9]
    sorted_arr = sorted(filtered_arr, reverse=True)
    result = [digit_names[x-1] for x in sorted_arr]
    
    return result
