def sum_squares(lst):
    
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i]**2
        elif i % 4 == 0:
            lst[i] = lst[i]**3
    for i in range(len(lst)):
        sum += lst[i]
    return sum

# Problem 3
