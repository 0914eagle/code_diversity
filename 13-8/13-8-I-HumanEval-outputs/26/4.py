
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to keep track of the numbers in lst1 that are not even
    odd_nums = set(num for num in lst1 if num % 2 != 0)
    
    # Iterate through lst2 and check if any of its elements can be added to lst1 to make all its elements even
    for num in lst2:
        if num % 2 == 0:
            # If the number is even, remove it from the set of odd numbers
            if num in odd_nums:
                odd_nums.remove(num)
        elif num % 2 != 0 and num - 1 in odd_nums:
            # If the number is odd and its previous number is in the set of odd numbers, remove both numbers from the set
            odd_nums.remove(num)
            odd_nums.remove(num - 1)
    
    # If the set of odd numbers is empty, it means all the elements of lst1 are even
    if not odd_nums:
        return "YES"
    else:
        return "NO"

