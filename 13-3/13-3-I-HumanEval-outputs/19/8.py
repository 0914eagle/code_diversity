
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
    # If not all the numbers in lst1 are even, check if any number in lst2 is even
    for num in lst2:
        if num % 2 == 0:
            # If any number in lst2 is even, add it to the set of even numbers and check if all the numbers in lst1 are even
            even_numbers.add(num)
            if len(even_numbers) == len(lst1):
                return "YES"
    # If no number in lst2 is even, return "NO"
    return "NO"

