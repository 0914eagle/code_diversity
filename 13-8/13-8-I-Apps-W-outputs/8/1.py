
def get_min_days(n, k, w):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the minimum number of days to 0
    min_days = 0
    
    # Loop through each pebble type
    for i in range(n):
        # Calculate the number of pebbles of the current type that Anastasia can collect in one day
        day_pebbles = k * (w[i] // k)
        
        # Update the minimum number of days needed to collect all the pebbles
        min_days += w[i] // day_pebbles
        
        # If there are remaining pebbles of the current type, add an extra day
        if w[i] % day_pebbles != 0:
            min_days += 1
    
    return min_days

