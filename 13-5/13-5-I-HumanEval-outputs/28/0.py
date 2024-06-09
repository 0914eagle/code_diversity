
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Loop through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
    # Loop through lst2 and check if any of the numbers are in the set of even numbers
    for num in lst2:
        if num in even_nums:
            # If any number is found, return "YES"
            return "YES"
    # If no number is found, return "NO"
    return "NO"

