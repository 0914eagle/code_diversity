
def speedcubing(t1, t2, t3, t4, t):
    # Calculate the average of the first four solves
    avg = (t1 + t2 + t3 + t4) / 4

    # Calculate the worst time Claire can have on her last solve to win the competition
    worst = avg + (t - avg) / 3

    # Check if Claire will win regardless of the time she gets on her last solve
    if worst <= t:
        return "infinite"

    # Check if it is possible for Claire to win the competition
    if worst > t:
        return "impossible"

    # Return the worst time Claire can have on her last solve to be declared the overall winner
    return f"{worst:.2f}"

