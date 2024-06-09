
def solve(n, c, a, b):
    # Initialize the minimum time to reach each floor as infinity
    min_time = [float('inf')] * (n + 1)
    # The minimum time to reach the first floor is 0
    min_time[1] = 0
    
    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible move from the current floor
        for j in range(1, n + 1):
            # If the move is using the stairs
            if i < j:
                # Calculate the minimum time to reach the current floor from the previous floor using the stairs
                time = min_time[i] + a[j - 1]
            else:
                # Calculate the minimum time to reach the current floor from the previous floor using the elevator
                time = min_time[i] + c + b[j - 1]
            # Update the minimum time to reach the current floor if necessary
            min_time[j] = min(min_time[j], time)
    
    return min_time[1:]

