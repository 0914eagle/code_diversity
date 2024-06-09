
def solve(W, v_h, N, x, y, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x[i], y[i])] = float('inf')
    
    # Initialize a dictionary to store the maximum horizontal speed required to pass through each gate
    max_speed = {}
    for i in range(N):
        max_speed[(x[i], y[i])] = float('-inf')
    
    # Loop through each gate and calculate the minimum time and maximum horizontal speed required to pass through it
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the distance between the two gates
            distance = abs(x[i] - x[j])
            
            # Calculate the time required to pass through the gate at each speed
            time_1 = distance / s[0]
            time_2 = distance / s[1]
            
            # Calculate the maximum horizontal speed required to pass through the gate
            speed_1 = v_h
            speed_2 = v_h + (s[1] - s[0]) * time_1 / distance
            
            # Update the minimum time and maximum horizontal speed required to pass through the gate
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], time_1)
            max_speed[(x[i], y[i])] = max(max_speed[(x[i], y[i])], speed_1)
            min_time[(x[j], y[j])] = min(min_time[(x[j], y[j])], time_2)
            max_speed[(x[j], y[j])] = max(max_speed[(x[j], y[j])], speed_2)
    
    # Loop through each gate and check if it is possible to pass through it with the selected skis
    for i in range(N):
        # Check if the gate is possible to pass through with the selected skis
        if min_time[(x[i], y[i])] > W or max_speed[(x[i], y[i])] > v_h:
            return "IMPOSSIBLE"
    
    # If all gates are possible to pass through, return the minimum time required to pass through the race course
    return min(s)

