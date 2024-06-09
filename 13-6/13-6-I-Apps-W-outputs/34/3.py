
def solve(a, b, x, y):
    # Initialize a dictionary to store the minimum time needed to reach each floor
    # The key is the floor number, and the value is the minimum time needed to reach that floor
    min_time = {1: 0}

    # Loop through each floor from 1 to 100
    for floor in range(1, 100):
        # If we have already calculated the minimum time to reach this floor, skip it
        if floor in min_time:
            continue

        # If we can reach this floor from the a-th floor of A, calculate the minimum time to reach it
        if floor - a <= 0:
            min_time[floor] = min_time[a] + abs(floor - a) * x

        # If we can reach this floor from the b-th floor of B, calculate the minimum time to reach it
        if floor - b <= 0:
            min_time[floor] = min_time[b] + abs(floor - b) * x

        # If we can reach this floor from both the a-th floor of A and the b-th floor of B, calculate the minimum time to reach it
        if floor - a <= 0 and floor - b <= 0:
            min_time[floor] = min(min_time[a] + abs(floor - a) * x, min_time[b] + abs(floor - b) * x)

    # Return the minimum time needed to reach the b-th floor of B from the a-th floor of A
    return min_time[b]

