
def solve(N, M, tunnels):
    # Initialize the danger level of each chamber as 0
    danger_level = [0] * (N + 1)

    # Loop through each tunnel
    for tunnel in tunnels:
        # Get the length of the tunnel
        length = tunnel[2]

        # Update the danger level of the starting chamber
        danger_level[tunnel[0]] += length

        # Update the danger level of the ending chamber
        danger_level[tunnel[1]] += length

    # Return the remainder of the danger level of each chamber when divided by 10^9 + 7
    return [danger_level[i] % (10**9 + 7) for i in range(1, N + 1)]

