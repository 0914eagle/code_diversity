
def solve(N, M, S, C):
    # Initialize the smallest integer as -1
    smallest_int = -1
    
    # Loop through all possible integers from 0 to 9^N-1
    for i in range(10**N):
        # Convert the current integer to a string
        curr_int_str = str(i)
        
        # Check if the current integer has the required number of digits
        if len(curr_int_str) != N:
            continue
        
        # Initialize a flag to indicate if all conditions are met
        all_conditions_met = True
        
        # Loop through all conditions
        for j in range(M):
            # Get the current digit and its position
            curr_digit = int(curr_int_str[S[j]-1])
            curr_pos = S[j]
            
            # Check if the current digit is equal to the required digit
            if curr_digit != C[j]:
                # If not, break the loop and continue to the next integer
                all_conditions_met = False
                break
        
        # If all conditions are met, update the smallest integer
        if all_conditions_met:
            smallest_int = i
            break
    
    # Return the smallest integer
    return smallest_int

