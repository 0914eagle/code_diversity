
from typing import List

def is_palindrome(lst: List[int]) -> bool:
    return lst == lst[::-1]

def will_it_fly(q: List[int], w: int) -> bool:
    if is_palindrome(q) and sum(q) <= w:
        return True
    return False

# Test the function with example inputs
print(will_it_fly([1, 2], 5))  # False
print(will_it_fly([3, 2, 3], 1))  # False
print(will_it_fly([3, 2, 3], 9))  # True
print(will_it_fly([3], 5))  # True
