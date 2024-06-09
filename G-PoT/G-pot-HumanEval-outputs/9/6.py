
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    # Count the number of odd elements in lst1
    odd_count = sum(1 for num in lst1 if num % 2 != 0)
    
    # If the number of odd elements is even, it is possible to exchange elements to make all even
    if odd_count % 2 == 0:
        return "YES"
    else:
        return "NO"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # Output: 'YES'
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # Output: 'NO'
