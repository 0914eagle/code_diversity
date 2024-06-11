def sum_squares(lst):
    
    # Initialize the sum variable
    sum = 0
    # Iterate through the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the value
        if i % 3 == 0:
            sum += lst[i] ** 2
        # If the index is a multiple of 4, cube the value
        elif i % 4 == 0:
            sum += lst[i] ** 3
        # Otherwise, add the value to the sum
        else:
            sum += lst[i]
    # Return the sum
    return sum


lst = [1,2,3]
print(sum_squares(lst))

lst = []
print(sum_squares(lst))

lst = [-1,-5,2,-1,-5]
print(sum_squares(lst))