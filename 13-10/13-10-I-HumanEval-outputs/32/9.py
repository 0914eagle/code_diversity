
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_numbers = set()
    # Iterate through the elements of lst1 and add only the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_numbers.add(num)
    # If all the elements of lst1 are even, return "YES"
    if len(even_numbers) == len(lst1):
        return "YES"
    # Initialize a dictionary to store the count of odd numbers in lst2
    odd_count = {}
    # Iterate through the elements of lst2 and increment the count of odd numbers
    for num in lst2:
        if num % 2 == 1:
            if num not in odd_count:
                odd_count[num] = 1
            else:
                odd_count[num] += 1
    # If there is an odd number in lst2 that is not in lst1, return "NO"
    for num in odd_count:
        if num not in even_numbers:
            return "NO"
    # If it is possible to exchange elements between lst1 and lst2 to make all the elements of lst1 even, return "YES"
    return "YES"

