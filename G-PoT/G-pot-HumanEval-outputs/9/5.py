
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # If the number of odd elements in lst1 is even, it is possible to exchange elements
    if odd_count % 2 == 0:
        return "YES"
    else:
        return "NO"
