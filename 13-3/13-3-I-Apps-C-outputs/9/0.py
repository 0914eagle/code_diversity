
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
            h_dist = abs(x[i] - x[j])
            # Calculate the vertical distance between the two gates
            v_dist = abs(y[i] - y[j])
            # Calculate the time required to pass through the gate
            time = h_dist / v_dist
            # Update the minimum time required to pass through the gate
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], time)
            min_time[(x[j], y[j])] = min(min_time[(x[j], y[j])], time)
    
    # Loop through each pair of skis and calculate the maximum horizontal speed at each gate
    for i in range(S):
        for j in range(N):
            # Calculate the horizontal distance between the gate and the starting point
            h_dist = abs(x[j] - W)
            # Calculate the time required to pass through the gate at the current speed
            time = h_dist / s[i]
            # Update the maximum horizontal speed at the gate if the time is less than the minimum time required to pass through the gate
            if time < min_time[(x[j], y[j])]:
                max_speed[(x[j], y[j])] = min(max_speed[(x[j], y[j])], s[i])
    
    # Loop through each gate and calculate the minimum time required to pass through it at the maximum horizontal speed
    min_time = float('inf')
    for i in range(N):
        min_time = min(min_time, min_time[(x[i], y[i])] * max_speed[(x[i], y[i])])
    
    # If the minimum time is infinite, it is impossible to complete the race with any pair of skis
    if min_time == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_time

