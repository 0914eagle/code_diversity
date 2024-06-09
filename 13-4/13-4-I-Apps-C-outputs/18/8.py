
def solve(N, M, tunnels):
    # Initialize the danger level of each chamber as 0
    danger_level = [0] * (N + 1)

    # Loop through each tunnel
    for tunnel in tunnels:
        # Get the length of the tunnel and the chambers it connects
        length, chamber1, chamber2 = tunnel

        # Update the danger level of both chambers
        danger_level[chamber1] += length
        danger_level[chamber2] += length

    # Return the remainder of the danger level of each chamber after dividing it by 10^9 + 7
    return [danger_level[i] % (10**9 + 7) for i in range(1, N + 1)]

