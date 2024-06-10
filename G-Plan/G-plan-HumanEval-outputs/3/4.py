
from typing import List

def is_palindrome(lst: List[int]) -> bool:
    return lst == lst[::-1]

def will_it_fly(q: List[int], w: int) -> bool:
    if is_palindrome(q) and sum(q) <= w:
        return True
    return False

# Input parsing
q = list(map(int, input().split()))
w = int(input())

# Output
print(will_it_fly(q, w))
