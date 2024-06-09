
def solve(N, M, conditions):
    # Initialize the smallest integer as -1
    smallest_int = -1
    
    # Iterate through all possible integers from 0 to 10^N-1
    for i in range(10**N):
        # Convert the integer to a string
        str_int = str(i)
        
        # Check if the integer has the correct number of digits
        if len(str_int) != N:
            continue
        
        # Check if the integer satisfies the conditions
        for s, c in conditions:
            if str_int[s-1] != str(c):
                break
        else:
            # If all conditions are satisfied, update the smallest integer
            smallest_int = min(smallest_int, i)
    
    # Return the smallest integer
    return smallest_int

