
def solve(v, a):
    # Convert the list of integers to a dictionary, where the key is the digit and the value is the amount of paint required
    paint_required = {i: a[i-1] for i in range(1, 10)}
    
    # Initialize the maximum number that can be written
    max_num = 0
    
    # Iterate through the digits from 1 to 9
    for i in range(1, 10):
        # Check if the current digit can be used
        if i != 0 and v >= paint_required[i]:
            # Subtract the amount of paint required for the current digit from the total amount of paint
            v -= paint_required[i]
            # Add the current digit to the maximum number that can be written
            max_num = max_num * 10 + i
    
    # If there is still enough paint left, add as many 9s as possible
    while v >= paint_required[9]:
        v -= paint_required[9]
        max_num = max_num * 10 + 9
    
    # If there is still enough paint left, add as many 0s as possible
    while v >= paint_required[0]:
        v -= paint_required[0]
        max_num = max_num * 10
    
    # If there is not enough paint for any digit, return -1
    if v > 0:
        return -1
    
    # Return the maximum number that can be written
    return max_num

