
def solve(W, v_h, N, x, y, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x[i], y[i])] = float('inf')
    
    # Initialize a dictionary to store the maximum horizontal speed at each gate
    max_speed = {}
    for i in range(N):
        max_speed[(x[i], y[i])] = v_h
    
    # Loop through each gate and calculate the minimum time required to pass through it
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the horizontal distance between the two gates
            dist = abs(x[i] - x[j])
            
            # Calculate the time required to pass through the gate at the current speed
            time = dist / s[i]
            
            # Update the minimum time required to pass through the gate
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], time)
            min_time[(x[j], y[j])] = min(min_time[(x[j], y[j])], time)
            
            # Update the maximum horizontal speed at the gate
            max_speed[(x[i], y[i])] = min(max_speed[(x[i], y[i])], s[i])
            max_speed[(x[j], y[j])] = min(max_speed[(x[j], y[j])], s[i])
    
    # Loop through each gate and calculate the minimum time required to pass through it with the maximum horizontal speed
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the horizontal distance between the two gates
            dist = abs(x[i] - x[j])
            
            # Calculate the time required to pass through the gate at the maximum speed
            time = dist / max_speed[(x[i], y[i])]
            
            # Update the minimum time required to pass through the gate
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], time)
            min_time[(x[j], y[j])] = min(min_time[(x[j], y[j])], time)
    
    # Calculate the total time required to pass through all the gates
    total_time = 0
    for i in range(N):
        total_time += min_time[(x[i], y[i])]
    
    # Return the speed of the pair of skis that allows you to get through the race course in the shortest time
    return s[total_time]

