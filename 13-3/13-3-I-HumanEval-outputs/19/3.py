
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
    # If all the numbers in lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Iterate through lst1 and add all the odd numbers to the set
    for num in lst1:
        if num % 2 == 1:
            odd_numbers.add(num)
    # If there are no odd numbers in lst1, return "NO"
    if not odd_numbers:
        return "NO"
    # Initialize a set to store the even numbers in lst2
    even_numbers_lst2 = set()
    # Iterate through lst2 and add all the even numbers to the set
    for num in lst2:
        if num % 2 == 0:
            even_numbers_lst2.add(num)
    # If there are no even numbers in lst2, return "NO"
    if not even_numbers_lst2:
        return "NO"
    # If the sum of the odd numbers in lst1 is greater than the sum of the even numbers in lst2, return "NO"
    if sum(odd_numbers) > sum(even_numbers_lst2):
        return "NO"
    # Otherwise, return "YES"
    return "YES"

