
def solve(n, m):
    # Calculate the number of possible hours and minutes
    num_hours = n
    num_minutes = m
    
    # Calculate the number of possible pairs of hour and minute
    num_pairs = num_hours * num_minutes
    
    # Return the number of pairs with distinct digits
    return num_pairs

