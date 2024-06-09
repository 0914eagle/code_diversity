
def solve(W, v_h, N, x, y, S, s):
    # Initialize the minimum time to pass through the course
    min_time = float('inf')
    # Initialize the minimum speed required to pass through the course
    min_speed = float('inf')

    # Loop through each pair of skis
    for i in range(S):
        # Calculate the horizontal speed required to pass through the course with the current pair of skis
        horizontal_speed = v_h
        if s[i] < horizontal_speed:
            horizontal_speed = s[i]

        # Calculate the time required to pass through the course with the current pair of skis
        time = 0
        for j in range(N):
            # Calculate the distance to the next gate
            distance = abs(x[j] - x[j-1])

            # Calculate the time required to pass through the current gate
            gate_time = distance / horizontal_speed

            # Add the time required to pass through the current gate to the total time
            time += gate_time

        # If the time required to pass through the course with the current pair of skis is less than the minimum time, update the minimum time and speed
        if time < min_time:
            min_time = time
            min_speed = s[i]

    # If it is impossible to pass through the course with any pair of skis, return "IMPOSSIBLE"
    if min_time == float('inf'):
        return "IMPOSSIBLE"

    # Otherwise, return the minimum speed required to pass through the course
    return min_speed

