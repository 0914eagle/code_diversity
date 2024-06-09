
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

    # If there are no odd numbers in lst1, return "YES"
    if not odd_numbers:
        return "YES"

    # If there are no even numbers in lst2, return "NO"
    if not even_numbers_lst2:
        return "NO"

    # If there are odd numbers in lst1 and even numbers in lst2,
    # check if it is possible to exchange elements to make all the elements of lst1 even
    for num in odd_numbers:
        if num + 1 in even_numbers_lst2:
            even_numbers.add(num + 1)
            odd_numbers.remove(num)
        elif num - 1 in even_numbers_lst2:
            even_numbers.add(num - 1)
            odd_numbers.remove(num)

    # If all the elements of lst1 are even, return "YES"
    if not odd_numbers:
        return "YES"
    else:
        return "NO"

