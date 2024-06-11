def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
  

    
    '''
    if (x == y + z) or (y == x + z) or (z == x + y):
        if (x == int(x)) and (y == int(y)) and (z == int(z)):
            return True
        else:
            return False
    else:
        return False

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))

# +
# 12.
# Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

# Examples
# sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17

# sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87

# sum_primes([]) ➞ None

# Notes
# Given numbers won't exceed 101.
# A prime number is a number which has exactly two divisors.

import math

