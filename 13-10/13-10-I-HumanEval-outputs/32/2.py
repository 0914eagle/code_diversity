
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Loop through lst1 and populate the sets
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    # Loop through lst2 and populate the sets
    for num in lst2:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    # Check if all the odd numbers in lst1 can be exchanged with even numbers in lst2
    for num in odd_numbers:
        if num * 2 not in even_numbers:
            return "NO"
    return "YES"

