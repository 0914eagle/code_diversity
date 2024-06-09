
def solve(a, b):
    # Initialize variables
    n = 0
    m = 0
    p = []
    q = []
    
    # Loop through all possible values of n
    for n in range(1, a+1):
        # Calculate the total time required to read n notes in the first day
        total_time = sum(range(1, n+1))
        
        # Check if the total time is less than or equal to a
        if total_time <= a:
            # Calculate the time required to read the last note in the first day
            last_note_time = total_time - n + 1
            
            # Check if the last note can be read in the second day
            if last_note_time <= b:
                # Calculate the time required to read the first note in the second day
                first_note_time = b - last_note_time + 1
                
                # Check if the first note can be read in the second day
                if first_note_time <= b:
                    # Add the first note to the list of notes to read in the first day
                    p.append(first_note_time)
                    
                    # Add the last note to the list of notes to read in the second day
                    q.append(last_note_time)
                    
                    # Break the loop
                    break
    
    # Return the maximum number of notes that can be read and the notes to read in each day
    return n, p, m, q

