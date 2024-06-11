def sum_squares(lst):
    
    # initialize the sum to 0
    sum = 0
    # loop through the list
    for i in range(len(lst)):
        # if the index is a multiple of 3, square the entry
        if i % 3 == 0:
            sum += lst[i] ** 2
        # if the index is a multiple of 4, cube the entry
        elif i % 4 == 0:
            sum += lst[i] ** 3
        # otherwise, add the entry as is
        else:
            sum += lst[i]
    # return the sum
    return sum
