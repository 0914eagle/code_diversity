
def solve(T, c, d):
    # Calculate the distance in kilometers
    distance = d / 1000
    
    # Initialize the total rain and sweat
    total_rain = 0
    total_sweat = 0
    
    # Loop through each minute interval
    for i in range(T):
        # Calculate the rain and sweat for this minute
        rain = rain_data[i]
        sweat = c * (velocity ** 2) * (distance / 1000)
        
        # Update the total rain and sweat
        total_rain += rain
        total_sweat += sweat
    
    # Return the total rain and sweat
    return total_rain + total_sweat

