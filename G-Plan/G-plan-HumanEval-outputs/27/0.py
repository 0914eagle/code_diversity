
from typing import List, Optional

def calculate_sign_product(arr: List[int]) -> int:
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
    return sum(abs(num) for num in arr)

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    sign_product = calculate_sign_product(arr)
    magnitude_sum = calculate_magnitude_sum(arr)
    return sign_product * magnitude_sum

# Test cases
print(prod_signs([1, 2, 2, -4]))
print(prod_signs([0, 1]))
print(prod_signs([]))
