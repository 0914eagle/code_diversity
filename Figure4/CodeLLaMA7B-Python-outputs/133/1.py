def sum_squares(lst):
    
    return sum([int(x**2) for x in lst])


print(sum_squares([1, 2, 3]))
print(sum_squares([1, 4, 9]))
print(sum_squares([1, 3, 5, 7]))
print(sum_squares([1.4, 4.2, 0]))
print(sum_squares([-2.4, 1, 1]))
