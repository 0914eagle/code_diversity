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
    if x == y + z and x.is_integer() and y.is_integer() and z.is_integer():
        return True
    elif y == x + z and x.is_integer() and y.is_integer() and z.is_integer():
        return True
    elif z == x + y and x.is_integer() and y.is_integer() and z.is_integer():
        return True
    else:
        return False

# +
# Challenge 3
# Create a function that takes a list of numbers.
# Return the largest number in the list.
# If the list is empty, return "No numbers".
# Examples
# findLargestNum([4, 5, 1, 3]) ➞ 5
# findLargestNum([300, 200, 600, 150]) ➞ 600
# findLargestNum([1000, 1001, 857, 1]) ➞ 1001
# findLargestNum([]) ➞ "No numbers"

# +
# Challenge 4
# Create a function that takes a list of strings.
# Return the words that are evenly spaced.
# Examples
# evenly_spaced(["cat", "laptop", "dog"]) ➞ ["cat", "dog"]
# evenly_spaced(["cat", "laptop", "dog", "computer"]) ➞ ["cat", "dog"]
# evenly_spaced(["cat", "laptop", "dog", "computer", "mouse"]) ➞ ["cat", "dog", "mouse"]
# evenly_spaced(["cat", "laptop", "dog", "computer", "mouse", "phone"]) ➞ ["cat", "dog", "mouse"]

# +
# Challenge 5
# Create a function that takes a list of numbers.
# Return the sum of all numbers in the list,
# but exclude any of the numbers that are divisible by 13.
# Return 0 if there are no numbers that can be summed.
# Examples
# sum_not_13([1, 2, 13, 21, 34, 55]) ➞ 110
# sum_not_13([