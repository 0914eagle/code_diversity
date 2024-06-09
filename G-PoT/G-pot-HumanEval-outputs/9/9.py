
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # If the number of odd elements in lst1 is even or lst2 has at least one even element, return "YES"
    if odd_count % 2 == 0 or any(num % 2 == 0 for num in lst2):
        return "YES"
    else:
        return "NO"
