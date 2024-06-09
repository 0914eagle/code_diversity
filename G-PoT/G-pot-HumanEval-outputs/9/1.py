
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    # Check if all elements in lst1 are already even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if there are odd numbers in lst2 that can be exchanged with odd numbers in lst1
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    odd_lst2 = [num for num in lst2 if num % 2 != 0]
    
    if len(odd_lst1) > len(odd_lst2):
        return "NO"
    
    return "YES"

# Test cases
print(exchange([1, 2, 3, 4], [1, 2, 3, 4]))  # 'YES'
print(exchange([1, 2, 3, 4], [1, 5, 3, 4]))  # 'NO'
