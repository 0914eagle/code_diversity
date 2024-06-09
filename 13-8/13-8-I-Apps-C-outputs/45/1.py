
def solve(T, c, d):
    # Calculate the distance that can be covered in each minute
    min_dist = (d / T) * 60
    
    # Initialize the variables for the dynamic programming
    rain = [0] * (T + 1)
    sweat = [0] * (T + 1)
    speed = [0] * (T + 1)
    
    # Dynamic programming to find the optimal strategy
    for i in range(1, T + 1):
        # Find the maximum rain and sweat for each minute
        max_rain = 0
        max_sweat = 0
        for j in range(i):
            max_rain = max(max_rain, rain[j])
            max_sweat = max(max_sweat, sweat[j])
        
        # Update the rain and sweat for the current minute
        rain[i] = max_rain
        sweat[i] = max_sweat + c * speed[i - 1] ** 2
        
        # Update the speed for the current minute
        speed[i] = min_dist / 60
    
    # Return the total rain and sweat
    return rain[T] + sweat[T]

