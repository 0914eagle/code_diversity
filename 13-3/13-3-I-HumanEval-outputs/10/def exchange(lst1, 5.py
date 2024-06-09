
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Initialize a set to store the even numbers in lst2
    even_numbers_lst2 = set()
    # Initialize a set to store the odd numbers in lst2
    odd_numbers_lst2 = set()

    # Iterate through lst1 and lst2 to find the even and odd numbers
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    for num in lst2:
        if num % 2 == 0:
            even_numbers_lst2.add(num)
        else:
            odd_numbers_lst2.add(num)

    # If all the elements of lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"

    # If there are no odd numbers in lst1, return "NO"
    if not odd_numbers:
        return "NO"

    # If there are no even numbers in lst2, return "NO"
    if not even_numbers_lst2:
        return "NO"

    # If it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 even, return "YES"
    if len(even_numbers_lst2) >= len(odd_numbers):
        return "YES"

    # Otherwise, return "NO"
    return "NO"

