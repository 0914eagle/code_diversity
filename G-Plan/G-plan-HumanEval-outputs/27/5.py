
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
    magnitude_sum = 0
    for num in arr:
        magnitude_sum += abs(num)
    return magnitude_sum

def prod_signs(arr: List[int]) -> Optional[int]:
    if not arr:
        return None
    
    sign_product = calculate_sign_product(arr)
    magnitude_sum = calculate_magnitude_sum(arr)
    
    return sign_product * magnitude_sum

input_arr = input().strip()
arr = list(map(int, input_arr.split(',')))
print(prod_signs(arr))
