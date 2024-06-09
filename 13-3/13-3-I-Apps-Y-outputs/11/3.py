
def solve(N, T):
    # Initialize a list to store the times when the hands point upward
    upward_times = []
    
    # Iterate through each clock
    for i in range(N):
        # Calculate the time when the hand of the current clock points upward
        upward_time = (360 // T[i]) * T[i]
        
        # Add the time to the list of upward times
        upward_times.append(upward_time)
    
    # Find the least common multiple (LCM) of all the upward times
    lcm = upward_times[0]
    for i in range(1, N):
        lcm = lcm(lcm, upward_times[i])
    
    # Return the least common multiple as the answer
    return lcm

# Find the least common multiple (LCM) of two numbers
def lcm(x, y):
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

