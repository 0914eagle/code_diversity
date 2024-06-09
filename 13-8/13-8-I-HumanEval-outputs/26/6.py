
from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    
    # Initialize a set to store the even numbers in lst1
    even_nums = set()
    # Initialize a set to store the odd numbers in lst1
    odd_nums = set()
    # Initialize a set to store the even numbers in lst2
    even_nums_lst2 = set()
    # Initialize a set to store the odd numbers in lst2
    odd_nums_lst2 = set()

    # Iterate through lst1 and lst2 and populate the sets
    for num in lst1:
        if num % 2 == 0:
            even_nums.add(num)
        else:
            odd_nums.add(num)
    for num in lst2:
        if num % 2 == 0:
            even_nums_lst2.add(num)
        else:
            odd_nums_lst2.add(num)

    # If all the odd numbers in lst1 can be found in lst2, return "YES"
    if odd_nums <= even_nums_lst2:
        return "YES"

    # If all the even numbers in lst1 can be found in lst2, return "YES"
    if even_nums <= even_nums_lst2:
        return "YES"

    # Otherwise, return "NO"
    return "NO"

