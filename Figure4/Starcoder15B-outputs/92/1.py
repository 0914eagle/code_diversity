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
        if (type(x) == int) and (type(y) == int) and (type(z) == int):
            return True
        else:
            return False
    else:
        return False

# +
# 2. Create a function that takes a list of numbers.
# Return the largest number in the list.

# Examples
# findLargestNum([4, 5, 1, 3]) ➞ 5
# findLargestNum([300, 200, 600, 150]) ➞ 600
# findLargestNum([1000, 1001, 857, 1]) ➞ 1001

