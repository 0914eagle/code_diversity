def sum_squares(lst):
    
    return sum(map(lambda x: x**2 if x % 3 == 0 else x**3 if x % 4 == 0 else x, lst))


print(sum_squares([1, 2, 3]))
print(sum_squares([]))
print(sum_squares([-1, -5, 2, -1, -5]))
