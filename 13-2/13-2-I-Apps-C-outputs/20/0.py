
def solve(W, v_h, N, x, y, S, s):
    # Initialize the minimum time to pass through the course
    min_time = float('inf')
    # Initialize the minimum speed required to pass through the course
    min_speed = 0

    # Loop through each pair of skis
    for i in range(S):
        # Calculate the horizontal speed required to pass through the course with the current pair of skis
        horizontal_speed = min(v_h, s[i])
        # Calculate the time required to pass through the course with the current pair of skis
        time = (y[-1] - y[0]) / s[i] + (x[-1] - x[0]) / horizontal_speed
        # Check if the time required is less than the minimum time
        if time < min_time:
            # Update the minimum time and speed
            min_time = time
            min_speed = s[i]

    # Check if it is possible to pass through the course with any pair of skis
    if min_time == float('inf'):
        return "IMPOSSIBLE"
    else:
        return min_speed

