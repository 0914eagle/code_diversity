
def solve(W, v_h, N, x, y, S, s):
    # Initialize a dictionary to store the minimum time required to pass through each gate
    min_time = {}
    for i in range(N):
        min_time[(x[i], y[i])] = float('inf')
    
    # Initialize a dictionary to store the minimum time required to pass through each gate with each pair of skis
    min_time_skis = {}
    for i in range(N):
        min_time_skis[(x[i], y[i])] = {s[j]: float('inf') for j in range(S)}
    
    # Initialize the minimum time required to pass through the first gate with each pair of skis
    for j in range(S):
        min_time_skis[(x[0], y[0])][s[j]] = s[j]
    
    # Loop through each gate
    for i in range(1, N):
        # Loop through each pair of skis
        for j in range(S):
            # Check if the current pair of skis can pass through the current gate
            if x[i] - W <= x[i-1] + v_h * min_time_skis[(x[i-1], y[i-1])][s[j]]:
                # Update the minimum time required to pass through the current gate with the current pair of skis
                min_time_skis[(x[i], y[i])][s[j]] = min(min_time_skis[(x[i], y[i])][s[j]], s[j] + min_time_skis[(x[i-1], y[i-1])][s[j]])
            else:
                # If the current pair of skis cannot pass through the current gate, set the minimum time to infinity
                min_time_skis[(x[i], y[i])][s[j]] = float('inf')
        
        # Update the minimum time required to pass through the current gate
        min_time[(x[i], y[i])] = min([min_time_skis[(x[i], y[i])][s[j]] for j in range(S)])
    
    # Find the pair of skis with the minimum time to pass through the last gate
    min_time_skis_last = min([min_time_skis[(x[N-1], y[N-1])][s[j]] for j in range(S)])
    
    # Check if it is possible to pass through all the gates with any pair of skis
    if min_time_skis_last == float('inf'):
        return "IMPOSSIBLE"
    
    # Find the pair of skis with the minimum time to pass through all the gates
    min_time_skis = min([min_time_skis[(x[i], y[i])][s[j]] for i in range(N) for j in range(S)])
    
    # Return the speed of the pair of skis with the minimum time to pass through all the gates
    return s[min_time_skis]

