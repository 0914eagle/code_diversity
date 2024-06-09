
from typing import List

def unique_digits(x: List[int]) -> List[int]:
    
    even_digits = [2, 4, 6, 8]
    unique_list = []
    for num in x:
        if num > 0:
            while num > 0:
                digit = num % 10
                if digit not in even_digits:
                    unique_list.append(num)
                    break
                num //= 10
    return sorted(set(unique_list))

