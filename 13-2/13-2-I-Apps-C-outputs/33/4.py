
def solve_small_y_puzzle(t, n):
    # Initialize the memoization dictionary
    memo = {}
    
    # Initialize the result variable
    result = 0
    
    # Iterate over the disks
    for i in range(n):
        # Calculate the cost of moving the current disk to the third rod
        cost = t[0][2] + t[1][2] + t[2][2]
        
        # If the cost is less than the current result, update the result
        if cost < result:
            result = cost
    
    # Return the result
    return result

