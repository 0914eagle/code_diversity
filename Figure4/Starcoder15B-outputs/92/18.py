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
    if type(x) == int and type(y) == int and type(z) == int:
        if x == y + z or x == y - z or x == z - y or x + y == z or x - y == z or x + z == y or x - z == y or y + z == x or y - z == x or y + x == z or y - x == z or z + x == y or z - x == y or z + y == x or z - y == x:
            return True
        else:
            return False
    else:
        return False

# +
# Test your function with the following test cases

print(any_int(5, 2, 7))
print(any_int(3, 2, 2))
print(any_int(3, -2, 1))
print(any_int(3.6, -2.2, 2))
# -

# ## 4.
#
# Create a function that takes a list of numbers and returns the sum of the two lowest positive numbers.
#
# Examples
#
# sum_two_smallest_nums([19, 5, 42, 2, 77]) ➞ 7
#
# sum_two_smallest_nums([10, 343445353, 3453445, 3453545353453]) ➞ 3453455
#
# sum_two_smallest_nums([2, 9, 6, -1]) ➞ 8
#
# sum_two_smallest_nums([879, 953, 694, -847, 342, 221, -91, -723, 791, -587]) ➞ 563
#
# sum_two_smallest_nums([3683, 2902, 3951, -475, 1617, -2385]) ➞ 4519
#
# Notes
#
# Don't count negative numbers.
# Floats and