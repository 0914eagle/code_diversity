
def solve(n, k, t):
    # Calculate the number of standing spectators at time t
    num_standing = (t // k) % 2
    
    # If the last spectator sits, reduce the number of standing spectators by 1
    if t % k == 0:
        num_standing -= 1
    
    return num_standing

