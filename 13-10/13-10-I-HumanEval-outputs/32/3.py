
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set(num for num in lst1 if num % 2 == 0)
    # Initialize a set to store the odd numbers in lst1
    odd_nums = set(num for num in lst1 if num % 2 == 1)
    # Iterate through lst2 and check if it contains any odd numbers
    for num in lst2:
        if num % 2 == 1:
            # If lst2 contains an odd number, check if it is in lst1
            if num in odd_nums:
                # If it is in lst1, remove it from lst1 and add it to even_nums
                odd_nums.remove(num)
                even_nums.add(num)
            else:
                # If it is not in lst1, return "NO"
                return "NO"
    # If all elements of lst1 are even, return "YES"
    if not odd_nums:
        return "YES"
    # If there are still odd numbers in lst1, return "NO"
    return "NO"

