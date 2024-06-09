
from typing import List

def double_the_difference(lst: List[float]) -> int:
    
    # Initialize an empty list to store the odd numbers
    odd_numbers = []
    
    # Iterate through the input list
    for num in lst:
        # Check if the number is an odd integer
        if num % 2 != 0 and num % 1 == 0:
            # Add the number to the list of odd numbers
            odd_numbers.append(num)
    
    # Initialize a variable to store the sum of squares of the odd numbers
    sum_of_squares = 0
    
    # Iterate through the list of odd numbers
    for num in odd_numbers:
        # Calculate the square of the number and add it to the sum
        sum_of_squares += num ** 2
    
    # Return the sum of squares of the odd numbers
    return sum_of_squares

