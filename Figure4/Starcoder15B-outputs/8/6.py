from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_of_numbers = 0
    product_of_numbers = 1
    for number in numbers:
        sum_of_numbers += number
        product_of_numbers *= number
    return sum_of_numbers, product_of_numbers


