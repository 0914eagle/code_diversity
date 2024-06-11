from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    if not numbers:
        return (0, 1)
    product = 1
    sum = 0
    for number in numbers:
        sum += number
        product *= number
    return (sum, product)


