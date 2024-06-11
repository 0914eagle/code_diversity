def sum_squares(lst):
    
    # Initialize the sum variable
    sum = 0
    
    # Iterate through the list
    for i in range(len(lst)):
        # If the index is a multiple of 3, square the entry
        if i % 3 == 0:
            sum += lst[i] ** 2
        # If the index is a multiple of 4, cube the entry
        elif i % 4 == 0:
            sum += lst[i] ** 3
        # Otherwise, do nothing
        else:
            pass
    
    # Return the sum
    return sum

# Run the function
print(sum_squares([1,2,3]))
print(sum_squares([]))