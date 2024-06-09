
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Iterate through lst1 and add all the even numbers to the set
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
    # If all the numbers in lst1 are even, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"
    # If not all the numbers in lst1 are even, check if we can make them all even by exchanging elements with lst2
    for num in lst1:
        if num % 2 == 1:
            # If the number is odd and there is an even number in lst2 that is not already in lst1, we can exchange them
            if num + 1 in lst2 and (num + 1) not in even_nums:
                even_nums.add(num + 1)
            # If the number is odd and there is no even number in lst2 that is not already in lst1, we cannot make it even
            else:
                return "NO"
    # If we can make all the numbers in lst1 even by exchanging elements with lst2, return "YES"
    if len(even_nums) == len(lst1):
        return "YES"
    # If we cannot make all the numbers in lst1 even by exchanging elements with lst2, return "NO"
    else:
        return "NO"

