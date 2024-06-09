
def solve(n, k, t):
    # Calculate the number of standing spectators at time t
    num_standing = (t // k) % 2
    
    # If the last spectator sits, subtract 1 from the number of standing spectators
    if t % k == 0:
        num_standing -= 1
    
    return num_standing

