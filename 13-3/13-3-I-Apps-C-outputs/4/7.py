
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

    # Return the danger level of each chamber
    return danger_level

