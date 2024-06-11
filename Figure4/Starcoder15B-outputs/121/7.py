def solution(lst):
    
    return sum(lst[1::2])

# +
# Test your function with the following

lst = [5, 8, 7, 1]
print(solution(lst))

lst = [3, 3, 3, 3, 3]
print(solution(lst))

lst = [30, 13, 24, 321]
print(solution(lst))
# -

# ## 2.
#
# Write a function that takes in a list of integers and returns the sum of the largest and smallest integers.
#
# Examples
#
# sum_largest_smallest([10, 4, 34, 6, 92, 2]) ==> 126
#
# sum_largest_smallest([-3, -5, -9, -1]) ==> -12
#
# sum_largest_smallest([2, 0, 2, 8, 10]) ==> 