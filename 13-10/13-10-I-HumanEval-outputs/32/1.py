
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Loop through the elements of lst1 and add the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
    # If all the elements of lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"
    # Loop through the elements of lst2 and check if any of them are in the set of even numbers
    for num in lst2:
        if num in even_nums:
            # If an even number is found in lst2, remove it from the set and check if the set is empty
            even_nums.remove(num)
            if len(even_nums) == 0:
                return "YES"
    # If no even number is found in lst2, return "NO"
    return "NO"

