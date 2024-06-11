def sum_squares(lst):
    
    lst = [int(x) for x in lst]
    lst = [x**2 for x in lst]
    return sum(lst)


lst = [1, 2, 3]
print(sum_squares(lst))
lst = [1, 4, 9]
print(sum_squares(lst))
lst = [1, 3, 5, 7]
print(sum_squares(lst))
lst = [1.4, 4.2, 0]
print(sum_squares(lst))
lst = [-2.4, 1, 1]
print(sum_squares(lst))
