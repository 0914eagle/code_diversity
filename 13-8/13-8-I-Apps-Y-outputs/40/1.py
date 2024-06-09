
def solve(N, M, constraints):
    # Initialize the smallest integer as -1
    smallest_int = -1
    
    # Iterate through all possible integers from 0 to 9^N-1
    for i in range(10**N):
        # Convert the current integer to a string
        curr_int_str = str(i)
        
        # Check if the current integer has the required number of digits
        if len(curr_int_str) != N:
            continue
        
        # Check if the current integer satisfies the constraints
        for j in range(M):
            s = constraints[j][0]
            c = constraints[j][1]
            if curr_int_str[s-1] != str(c):
                break
        else:
            # If the current integer satisfies all the constraints, check if it is the smallest so far
            if smallest_int == -1 or i < smallest_int:
                smallest_int = i
    
    return smallest_int

