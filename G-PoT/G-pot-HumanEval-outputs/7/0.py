
from typing import List

def by_length(arr: List[int]) -> List[str]:
    digit_names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    filtered_arr.sort(reverse=True)
    
    result = [digit_names[num - 1] for num in filtered_arr]
    
    return result
