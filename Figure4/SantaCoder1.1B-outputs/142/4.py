def sum_squares(lst):
    
    # Your code here
    return sum(map(lambda x: x**2 if x%3==0 else x**3 if x%4==0 else x, lst))

