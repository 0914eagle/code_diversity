
def solve(n, k, pebbles):
    # Number of days needed to collect all pebbles
    days = 0
    
    # Number of pebbles collected on each day
    collected = [0] * n
    
    # Sort pebbles in descending order
    pebbles.sort(reverse=True)
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles that can be collected on this day
        num_collected = min(pebbles[i], k)
        
        # Update the number of pebbles collected on this day
        collected[i] += num_collected
        
        # Update the number of pebbles left to collect
        pebbles[i] -= num_collected
        
        # If all pebbles of this type have been collected, move on to the next type
        if pebbles[i] == 0:
            continue
        
        # Increment the number of days needed to collect all pebbles
        days += 1
    
    return days

