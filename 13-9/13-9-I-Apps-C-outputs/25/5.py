
def min_seconds_to_make_alice_happy(n, a):
    # Initialize a variable to store the minimum number of seconds
    seconds = 0
    
    # Initialize a variable to store the number of positive values in the array
    positive_values = 0
    
    # Iterate through the array
    for i in range(n):
        # If the current value is positive, increment the number of positive values
        if a[i] > 0:
            positive_values += 1
    
    # If there is only one positive value, return -1 because Alice will not be happy
    if positive_values == 1:
        return -1
    
    # Initialize a variable to store the minimum number of chocolates in a box
    min_chocolates = float('inf')
    
    # Initialize a variable to store the maximum number of chocolates in a box
    max_chocolates = 0
    
    # Iterate through the array
    for i in range(n):
        # If the current value is positive, update the minimum and maximum numbers of chocolates
        if a[i] > 0:
            min_chocolates = min(min_chocolates, a[i])
            max_chocolates = max(max_chocolates, a[i])
    
    # Calculate the number of seconds needed to make Alice happy
    seconds = (max_chocolates - min_chocolates) // (positive_values - 1)
    
    # Return the number of seconds
    return seconds

