
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Iterate through the elements of lst1 and add the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
    # If all the elements of lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    # If not all the elements of lst1 are even, try to find a pair of numbers in lst2 that can be exchanged with an even number in lst1 to make all the elements of lst1 even
    for num in lst2:
        if num % 2 == 0 and num not in even_numbers:
            even_numbers.add(num)
            break
    # If a pair of numbers can be found, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    # If no pair of numbers can be found, return "NO"
    return "NO"

