
def solve(n, k, t):
    # Calculate the number of standing spectators at time t
    standing_spectators = (t // k) % 2

    # If the last spectator sits, subtract 1 from the number of standing spectators
    if t % k == 0:
        standing_spectators -= 1

    return standing_spectators

