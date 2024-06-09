
def solve(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days needed to collect all pebbles as 0
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that can be collected in one day
        day_pebbles = k * (w[i] // k)
        
        # If the number of pebbles of the current type is less than the number that can be collected in one day, then collect all the pebbles of the current type in one day
        if w[i] < day_pebbles:
            days += 1
            w[i] = 0
        # Otherwise, collect as many pebbles of the current type as possible in one day and subtract the number of pebbles collected from the total number of pebbles
        else:
            days += 1
            w[i] -= day_pebbles
            total_pebbles -= day_pebbles
    
    # Return the number of days needed to collect all pebbles
    return days

