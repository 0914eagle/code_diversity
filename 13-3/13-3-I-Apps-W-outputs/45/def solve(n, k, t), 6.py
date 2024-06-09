
def solve(n, k, t):
    # Calculate the number of standing spectators at time t
    standing = (t // k) % 2

    # Return the result
    return standing

