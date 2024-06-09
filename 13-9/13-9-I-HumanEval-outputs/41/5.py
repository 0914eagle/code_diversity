
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    # convert list to string
    x_str = [str(i) for i in x]
    
    # check if any digit is even
    even_digits = [int(i) for i in x_str if '0' in i or '2' in i or '4' in i or '6' in i or '8' in i]
    
    # return sorted list of unique digits
    return sorted(set([int(i) for i in x_str if i not in even_digits]))

