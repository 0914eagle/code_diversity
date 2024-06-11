def sum_squares(lst):
    
    lst = [int(x) for x in lst]
    lst = [int(x**2) for x in lst]
    return sum(lst)
