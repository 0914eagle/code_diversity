
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    # Check if lst1 already consists of only even numbers
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are odd numbers in lst2 that can be exchanged with lst1
    for num in lst2:
        if num % 2 == 0:
            return "YES"
    
    return "NO"
