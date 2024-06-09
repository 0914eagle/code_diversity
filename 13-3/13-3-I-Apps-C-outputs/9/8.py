
def solve(W, v_h, N, x, y, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x[i], y[i])] = float('inf')
    
    # Initialize a dictionary to store the minimum time required to pass through each gate with a specific speed
    min_time_with_speed = {}
    for i in range(N):
        min_time_with_speed[(x[i], y[i])] = float('inf')
    
    # Loop through each gate and calculate the minimum time required to pass through it
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the horizontal distance between the two gates
            horizontal_distance = abs(x[i] - x[j])
            # Calculate the vertical distance between the two gates
            vertical_distance = abs(y[i] - y[j])
            # Calculate the time required to pass through the gate
            time = horizontal_distance / v_h + vertical_distance / s[i]
            # Update the minimum time required to pass through the gate
            min_time[(x[i], y[i])] = min(min_time[(x[i], y[i])], time)
    
    # Loop through each gate and calculate the minimum time required to pass through it with a specific speed
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the horizontal distance between the two gates
            horizontal_distance = abs(x[i] - x[j])
            # Calculate the vertical distance between the two gates
            vertical_distance = abs(y[i] - y[j])
            # Calculate the time required to pass through the gate with the specified speed
            time = horizontal_distance / v_h + vertical_distance / s[i]
            # Update the minimum time required to pass through the gate with the specified speed
            min_time_with_speed[(x[i], y[i])] = min(min_time_with_speed[(x[i], y[i])], time)
    
    # Initialize the minimum time required to pass through the course
    min_time_course = float('inf')
    # Loop through each gate and calculate the minimum time required to pass through the course with a specific speed
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the time required to pass through the course with the specified speed
            time = min_time_with_speed[(x[i], y[i])] + min_time_with_speed[(x[j], y[j])]
            # Update the minimum time required to pass through the course
            min_time_course = min(min_time_course, time)
    
    # Check if it is possible to pass through the course with any pair of skis
    if min_time_course == float('inf'):
        return "IMPOSSIBLE"
    
    # Initialize the minimum speed required to pass through the course
    min_speed = float('inf')
    # Loop through each gate and calculate the minimum speed required to pass through the course
    for i in range(N):
        for j in range(i+1, N):
            # Calculate the time required to pass through the course with the specified speed
            time = min_time[(x[i], y[i])] + min_time[(x[j], y[j])]
            # Update the minimum speed required to pass through the course
            min_speed = min(min_speed, s[i])
    
    # Return the minimum speed required to pass through the course
    return min_speed

