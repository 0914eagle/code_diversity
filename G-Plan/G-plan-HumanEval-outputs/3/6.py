
from typing import List

def is_palindrome(lst: List[int]) -> bool:
    return lst == lst[::-1]

def will_it_fly(q: List[int], w: int) -> bool:
    if is_palindrome(q) and sum(q) <= w:
        return True
    return False

# Test cases
print(will_it_fly([1, 2], 5))
print(will_it_fly([3, 2, 3], 1))
print(will_it_fly([3, 2, 3], 9))
print(will_it_fly([3], 5))
