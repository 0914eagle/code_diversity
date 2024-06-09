
def solve_rubiks_cube(t1, t2, t3, t4, t):
    # Calculate the average of the first four solves
    avg = (t1 + t2 + t3 + t4) / 4

    # Calculate the worst time Claire can have on her last solve to win the competition
    worst_time = avg - t

    # Check if it is possible for Claire to win the competition
    if worst_time <= 0:
        return "impossible"

    # Return the worst time Claire can have on her last solve to win the competition
    return round(worst_time, 2)

