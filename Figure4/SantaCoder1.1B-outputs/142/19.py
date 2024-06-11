def sum_squares(lst):
    
    sum_of_squares = 0
    for i in lst:
        if i % 3 == 0:
            sum_of_squares += i ** 2
        elif i % 4 == 0:
            sum_of_squares += i ** 3
    return sum_of_squares

