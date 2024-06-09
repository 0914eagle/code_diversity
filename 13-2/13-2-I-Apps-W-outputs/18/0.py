
def solve(a, b):
    # Initialize variables
    n = 0
    m = 0
    p = []
    q = []
    
    # Loop through all possible values of n
    for n in range(1, a+1):
        # Calculate the total time required to read n notes in the first day
        time_first_day = sum(range(1, n+1))
        
        # Check if the total time required is less than or equal to a
        if time_first_day <= a:
            # Calculate the total time required to read m notes in the second day
            time_second_day = a - time_first_day
            
            # Check if the total time required is less than or equal to b
            if time_second_day <= b:
                # Calculate the number of notes that can be read in the second day
                m = b - time_second_day
                
                # Add the notes that can be read in the second day to the list q
                q = list(range(n+1, n+m+1))
                
                # Break out of the loop
                break
    
    # Return the results
    return n, p, m, q

