
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
            # If any number in lst2 is even, remove it from the set and add the number to the set
            even_numbers.add(num)
            even_numbers.remove(num)
            # If after removing and adding the number, the set has the same length as lst1, return "YES"
            if len(even_numbers) == len(lst1):
                return "YES"
    # If none of the numbers in lst2 are even, return "NO"
    return "NO"

