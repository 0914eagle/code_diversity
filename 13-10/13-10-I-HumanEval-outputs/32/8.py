
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Initialize a set to store the odd numbers in lst1
    odd_numbers = set()
    # Initialize a set to store the numbers in lst2
    numbers = set(lst2)
    
    # Iterate through lst1 and add even and odd numbers to their respective sets
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
        else:
            odd_numbers.add(num)
    
    # If all the numbers in lst1 are even, return "YES"
    if not odd_numbers:
        return "YES"
    
    # If there are no even numbers in lst1, return "NO"
    if not even_numbers:
        return "NO"
    
    # Iterate through the even numbers in lst1 and check if there is a corresponding odd number in lst2
    for even_num in even_numbers:
        if even_num + 1 in numbers:
            return "YES"
    
    # If no corresponding odd number is found, return "NO"
    return "NO"

