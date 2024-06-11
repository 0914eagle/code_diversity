def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    # Your code here
    lst.sort()
    lst.reverse()
    for i in lst:
        if lst.count(i) >= i:
            return i
    return -1

print(search([4, 1, 2, 2, 3, 1]))
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
print(search([5, 5, 4, 4, 4]))

# +
# 2.
# Write a function that takes a list of integers and returns the sum of the squares of all the odd numbers.
# Examples:
#     sum_odd_squares([1, 2, 3, 4, 5]) == 35
#     sum_odd_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 189

# +
# 3.
# Write a function that takes a list of integers and returns the sum of the squares of all the odd numbers.
# Examples:
#     sum_odd_squares([1, 2, 3, 4, 5]) == 35
#     sum_odd_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 189

# +
# 4.
# Write a function that takes a list of integers and returns the sum of the squares of all the odd numbers.
# Examples:
#     sum_odd_squares([1, 2, 3, 4, 5]) == 35
#     sum_odd_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 189

# +
# 5.
# Write a function that takes a list of integers and returns the sum of the squares of all the odd numbers.
# Examples:
#     sum_odd_squares([1, 2, 3, 4, 5]) == 35
#     sum_odd_squares([1, 