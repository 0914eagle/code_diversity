
def solve(a, b):
    # Initialize variables
    notes_read_today = 0
    notes_read_tomorrow = 0
    notes_to_read_today = []
    notes_to_read_tomorrow = []
    
    # Iterate through all possible notes
    for i in range(1, a+b+1):
        # Check if the note can be read today
        if i <= a:
            notes_to_read_today.append(i)
            notes_read_today += 1
        # Check if the note can be read tomorrow
        if i <= b:
            notes_to_read_tomorrow.append(i)
            notes_read_tomorrow += 1
    
    # Return the maximum number of notes that can be read
    return notes_read_today, notes_to_read_today, notes_read_tomorrow, notes_to_read_tomorrow

