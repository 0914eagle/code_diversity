from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    
    sum_ = 0
    product = 1
    for number in numbers:
        sum_ += number
        product *= number
    return sum_, product
/tests/test_task_0002.py
from tasks.task_0002 import sum_product


