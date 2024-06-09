
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
    # If all the elements of lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"
    # If not all the elements of lst1 are even, check if there are any even numbers in lst2 that can be exchanged with odd numbers in lst1
    for num in lst2:
        if num % 2 == 0 and num not in even_nums:
            # If there is an even number in lst2 that is not in lst1, return "YES"
            return "YES"
    # If no even number in lst2 can be exchanged with an odd number in lst1, return "NO"
    return "NO"

