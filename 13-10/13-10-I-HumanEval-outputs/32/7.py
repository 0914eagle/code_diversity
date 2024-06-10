
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    

    # Initialize a set to keep track of the even numbers in lst1
    even_nums = set()

    # Loop through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)

    # Loop through lst2 and remove all the numbers that are not in the set of even numbers
    for i in range(len(lst2) - 1, -1, -1):
        if lst2[i] not in even_nums:
            lst2.pop(i)

    # If all the numbers in lst1 are even, return "YES"
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    else:
        return "NO"

