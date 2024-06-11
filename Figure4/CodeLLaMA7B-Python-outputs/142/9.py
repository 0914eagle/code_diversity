def sum_squares(lst):
    
    # Initialize the sum variable
    sum = 0
    # Iterate through the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the integer
        if i % 3 == 0:
            sum += lst[i] ** 2
        # If the index is a multiple of 4, cube the integer
        elif i % 4 == 0:
            sum += lst[i] ** 3
        # If the index is not a multiple of 3 or 4, do not change the integer
        else:
            sum += lst[i]
    # Return the sum
    return sum


# Test the function with examples provided in the instructions
print(sum_squares([1,2,3]))
print(sum_squares([]))
print(sum_squares([-1,-5,2,-1,-5]))

# Test the function with my own examples
print(sum_squares([1,2,3,4,5,6,7,8,9,10]))
print(sum_squares([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))

