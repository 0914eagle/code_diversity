
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Initialize a set to store the odd numbers in lst1
    odd_nums = set()
    # Initialize a set to store the even numbers in lst2
    even_nums_2 = set()
    # Initialize a set to store the odd numbers in lst2
    odd_nums_2 = set()

    # Iterate through lst1 and lst2 and populate the sets
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
        else:
            odd_nums.add(num)
    for num in lst2:
        if num % 2 == 0:
            even_nums_2.add(num)
        else:
            odd_nums_2.add(num)

    # If all the elements of lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"

    # If there are no odd numbers in lst1, return "NO"
    if not odd_nums:
        return "NO"

    # If there are no even numbers in lst2, return "NO"
    if not even_nums_2:
        return "NO"

    # If the number of odd numbers in lst1 is greater than the number of even numbers in lst2, return "NO"
    if len(odd_nums) > len(even_nums_2):
        return "NO"

    # If the number of odd numbers in lst1 is equal to the number of even numbers in lst2, return "YES"
    if len(odd_nums) == len(even_nums_2):
        return "YES"

    # If the number of odd numbers in lst1 is less than the number of even numbers in lst2, return "YES"
    return "YES"

