
def get_min_days(w, k):
    # Calculate the total number of pebbles
    total_pebbles = sum(w)
    
    # Initialize the number of days needed to collect all pebbles as 0
    days = 0
    
    # Loop through each pebble type
    for i in range(len(w)):
        # Calculate the number of pebbles of the current type that can be collected in one day
        day_pebbles = k // w[i]
        
        # If the number of pebbles of the current type is less than the number that can be collected in one day, set the number of pebbles to collect as the number of pebbles of the current type
        if day_pebbles > w[i]:
            day_pebbles = w[i]
        
        # Add the number of days needed to collect the current type of pebbles to the total number of days
        days += w[i] // day_pebbles
        
        # If there are remaining pebbles of the current type, add an extra day
        if w[i] % day_pebbles != 0:
            days += 1
    
    return days

