
def solve(N, T):
    # Initialize a list to store the time it takes for each clock to point upward
    times = []
    
    # Loop through each clock
    for i in range(N):
        # Calculate the time it takes for the clock to point upward
        time = (360 * (i + 1)) // N
        
        # Add the time to the list
        times.append(time)
    
    # Find the least common multiple (LCM) of all the times
    lcm = 1
    for time in times:
        lcm = lcm_of_two_numbers(lcm, time)
    
    # Return the LCM
    return lcm

# Function to find the least common multiple (LCM) of two numbers
def lcm_of_two_numbers(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    
    while(True):
        if(greater % x == 0 and greater % y == 0):
            lcm = greater
            break
        greater += 1
    
    return lcm

