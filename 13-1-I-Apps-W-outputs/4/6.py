
def solve_rubiks_cube(t1, t2, t3, t4, t):
    # Calculate the average of the first four solves
    avg = (t1 + t2 + t3 + t4) / 4

    # Calculate the worst time Claire can have on her last solve to win the competition
    worst_time = avg + (t - avg) / 3

    # Check if the worst time is less than or equal to the target time
    if worst_time <= t:
        return worst_time
    else:
        return "impossible"

