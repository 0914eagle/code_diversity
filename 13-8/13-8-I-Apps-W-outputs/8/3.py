
def solve(n, k, pebbles):
    # Calculate the total number of pebbles
    total_pebbles = sum(pebbles)
    
    # Initialize the number of days needed to collect all pebbles
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that Anastasia can collect in one day
        day_pebbles = min(k, pebbles[i])
        
        # Update the number of days needed to collect all pebbles
        days += (pebbles[i] - 1) // day_pebbles + 1
    
    # Return the minimum number of days needed to collect all pebbles
    return days

