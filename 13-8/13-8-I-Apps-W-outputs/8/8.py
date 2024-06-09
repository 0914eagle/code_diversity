
def solve(n, k, pebbles):
    # Calculate the total number of pebbles
    total_pebbles = sum(pebbles)
    
    # Initialize the number of days needed to collect all pebbles
    days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that can be collected on this day
        current_pebbles = min(pebbles[i], k)
        
        # Update the number of days needed to collect all pebbles
        days += (current_pebbles - 1) // k + 1
        
        # Update the number of pebbles of the current type that are left to collect
        pebbles[i] -= current_pebbles
    
    # Return the minimum number of days needed to collect all pebbles
    return days

