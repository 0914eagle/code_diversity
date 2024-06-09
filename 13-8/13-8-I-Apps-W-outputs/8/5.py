
def solve(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days needed to collect all pebbles to 0
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that Anastasia can collect in one day
        day_pebbles = min(k, w[i])
        
        # Update the number of days needed to collect all pebbles
        days += (w[i] - 1) // day_pebbles + 1
    
    # Return the minimum number of days needed to collect all pebbles
    return days

