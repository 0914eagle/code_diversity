
def solve(N, M, conditions):
    # Initialize the smallest integer as -1
    smallest_int = -1
    
    # Loop through all possible integers from 0 to 9^N-1
    for i in range(10**N):
        # Convert the current integer to a string
        curr_int_str = str(i)
        
        # Check if the current integer has the required number of digits
        if len(curr_int_str) != N:
            continue
        
        # Check if the current integer satisfies the conditions
        is_satisfied = True
        for s, c in conditions:
            if curr_int_str[s-1] != str(c):
                is_satisfied = False
                break
        
        # If the current integer satisfies the conditions, check if it is smaller than the current smallest integer
        if is_satisfied and smallest_int == -1:
            smallest_int = i
        elif is_satisfied and i < smallest_int:
            smallest_int = i
    
    # Return the smallest integer
    return smallest_int

