
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

def calculate_magnitude_sum(arr: List[int]) -> int:
    magnitude_sum = 0
    for num in arr:
        magnitude_sum += abs(num)
    return magnitude_sum

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    product_of_signs = calculate_product_of_signs(arr)
    magnitude_sum = calculate_magnitude_sum(arr)
    return product_of_signs * magnitude_sum

# Test the function with example inputs
print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
