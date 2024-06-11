def sum_squares(lst):
    
    # Solution 1
    return sum([pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x for i, x in enumerate(lst)])
    
    # Solution 2
    # return sum(map(lambda x: pow(x, 3) if i % 4 == 0 and i % 3 != 0 else pow(x, 2) if i % 3 == 0 else x, lst))
    
    # Solution 3
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 4
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 5
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 6
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 7
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 8
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else 1), lst))
    
    # Solution 9
    # return sum(map(lambda x: x ** (3 if i % 4 == 0 and i % 3 != 0 else 2 if i % 3 == 0 else