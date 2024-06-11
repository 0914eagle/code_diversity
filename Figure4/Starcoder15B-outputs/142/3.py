def sum_squares(lst):
    
    # YOUR CODE HERE
    sum = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            lst[i] = lst[i]**2
        elif i % 4 == 0:
            lst[i] = lst[i]**3
    for i in lst:
        sum += i
    return sum


#