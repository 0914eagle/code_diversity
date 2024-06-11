def sum_squares(lst):
    
    return sum([x**2 for x in lst if x % 3 == 0 or x % 4 == 0])

