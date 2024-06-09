
def solve(a, b):
    # Initialize the maximum number of notes that can be read
    max_notes = 0
    # Initialize the number of notes to read in the first day
    n = 0
    # Initialize the number of notes to read in the second day
    m = 0
    # Initialize the list of notes to read in the first day
    p = []
    # Initialize the list of notes to read in the second day
    q = []
    
    # Iterate through all possible combinations of notes to read
    for i in range(1, a+1):
        for j in range(1, b+1):
            # Calculate the total number of hours needed to read the current combination of notes
            total_hours = i + j
            # Check if the current combination of notes is the maximum possible
            if total_hours > max_notes:
                # Update the maximum number of notes that can be read
                max_notes = total_hours
                # Update the number of notes to read in the first day
                n = i
                # Update the number of notes to read in the second day
                m = j
                # Update the list of notes to read in the first day
                p = list(range(1, n+1))
                # Update the list of notes to read in the second day
                q = list(range(n+1, n+m+1))
    
    # Return the maximum number of notes that can be read and the lists of notes to read in the first and second days
    return max_notes, p, m, q

