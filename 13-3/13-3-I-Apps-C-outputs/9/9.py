
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
            dx = x[j] - x[i]
            dy = y[j] - y[i]
            if dy != 0:
                t = dx / dy
                if t < min_time[(x[i], y[i])]:
                    min_time[(x[i], y[i])] = t
                if t > max_speed[(x[i], y[i])]:
                    max_speed[(x[i], y[i])] = t
    
    # Loop through each pair of skis and calculate the minimum time required to pass through all the gates with that pair of skis
    for i in range(S):
        time = 0
        for j in range(N):
            time += min_time[(x[j], y[j])] / s[i]
        if time < float('inf'):
            return s[i]
    
    return -1

