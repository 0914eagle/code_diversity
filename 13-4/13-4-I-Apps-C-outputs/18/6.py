
import sys
import math

def get_danger_level(chambers, tunnels):
    # Initialize the danger level of each chamber as 0
    danger_level = [0] * len(chambers)

    # Loop through each tunnel
    for tunnel in tunnels:
        # Get the length of the tunnel
        length = tunnel[2]

        # Get the start and end chambers of the tunnel
        start_chamber = tunnel[0]
        end_chamber = tunnel[1]

        # Update the danger level of the start chamber
        danger_level[start_chamber - 1] += length

        # Update the danger level of the end chamber
        danger_level[end_chamber - 1] += length

    return danger_level

def main():
    # Read the number of chambers and tunnels
    num_chambers, num_tunnels = map(int, input().split())

    # Read the tunnels
    tunnels = []
    for _ in range(num_tunnels):
        tunnel = list(map(int, input().split()))
        tunnels.append(tunnel)

    # Get the danger level of each chamber
    danger_level = get_danger_level(range(1, num_chambers + 1), tunnels)

    # Print the danger level of each chamber
    for level in danger_level:
        print(level % (10**9 + 7))

if __name__ == "__main__":
    main()

