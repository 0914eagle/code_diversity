
from typing import List, Optional

def calculate_product_of_signs(arr: List[int]) -> int:
    product = 1
    for num in arr:
        if num > 0:
            product *= 1
        elif num < 0:
            product *= -1
        else:
            product *= 0
    return product

def calculate_sum_of_magnitudes(arr: List[int]) -> int:
    return sum(map(abs, arr))

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    
    product_of_signs = calculate_product_of_signs(arr)
    sum_of_magnitudes = calculate_sum_of_magnitudes(arr)
    
    return sum_of_magnitudes * product_of_signs

# Test cases
print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
